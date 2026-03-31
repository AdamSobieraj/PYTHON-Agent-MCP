"""
docling_pdf_parser.py

Parser PDF → Markdown oparty na IBM Docling z akceleracją GPU.

Trójwarstwowe usuwanie nagłówków/stopek stron:
  1. PRE-CROP  — fizyczne przycięcie marginesów (PyMuPDF cropbox)
  2. SEMANTIC  — Docling rozpoznaje PAGE_HEADER / PAGE_FOOTER
  3. POST-FILTER — filtr po pozycji bounding box (fallback bez fitz)

Wymaga:
    pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121
    pip install docling easyocr langchain-core pymupdf
"""

import io
import logging
import os
from collections import defaultdict
from typing import Dict, List, Optional, Tuple, Union
from docling.datamodel.base_models import InputFormat
from docling.datamodel.document import DocumentStream
from docling.datamodel.pipeline_options import (
    AcceleratorDevice,
    AcceleratorOptions,
    EasyOcrOptions,
    PdfPipelineOptions,
    TableFormerMode,
    TableStructureOptions,
)
from docling.document_converter import DocumentConverter, PdfFormatOption
import torch
from langchain_core.documents import Document

from base_parser import BaseDocumentParser

logger = logging.getLogger(__name__)

# ── Opcjonalna zależność: PyMuPDF (do fizycznego cropowania) ──────
try:
    import fitz

    FITZ_AVAILABLE = True
except ImportError:
    FITZ_AVAILABLE = False
    logger.info(
        "PyMuPDF (fitz) niedostępny → obcinanie marginesów przez post-filtr bbox. "
        "Dla najlepszych rezultatów zainstaluj: pip install pymupdf"
    )


class PdfParser(BaseDocumentParser):
    """
    Parser PDF oparty na IBM Docling z akceleracją GPU
    i trójwarstwowym usuwaniem nagłówków/stopek.

    Marginesy podawane w punktach typograficznych (1 pt = 1/72 cala).
    Standardowa strona A4: 595 × 842 pt.

    Typowe wartości:
        top_margin_crop=50   — usuwa nagłówek (~1.8 cm)
        bottom_margin_crop=60 — usuwa stopkę z numeracją (~2.1 cm)
    """

    # Etykiety do pominięcia (warstwa semantyczna)
    SKIP_LABELS: set = {"page_header", "page_footer"}

    def __init__(
        self,
        use_gpu: bool = True,
        do_ocr: bool = True,
        ocr_languages: Optional[List[str]] = None,
        table_mode: str = "accurate",
        num_threads: int = 4,
        top_margin_crop: float = 50.0,
        bottom_margin_crop: float = 60.0,
        left_margin_crop: float = 0.0,
        right_margin_crop: float = 0.0,
    ):
        """
        Args:
            use_gpu:              Czy używać GPU (auto-fallback na CPU).
            do_ocr:               Czy uruchamiać OCR (dla skanów).
            ocr_languages:        Języki OCR (domyślnie ["pl", "en"]).
            table_mode:           "accurate" (GPU) lub "fast" (CPU ok).
            num_threads:          Wątki CPU.
            top_margin_crop:      Górny margines do obcięcia [pt].
            bottom_margin_crop:   Dolny margines do obcięcia [pt].
            left_margin_crop:     Lewy margines do obcięcia [pt].
            right_margin_crop:    Prawy margines do obcięcia [pt].
        """
        # ── Marginesy ────────────────────────────────────────────
        self._top_margin = top_margin_crop
        self._bottom_margin = bottom_margin_crop
        self._left_margin = left_margin_crop
        self._right_margin = right_margin_crop
        self._margins_enabled = any(
            [top_margin_crop, bottom_margin_crop, left_margin_crop, right_margin_crop]
        )

        if self._margins_enabled:
            crop_method = "pre-crop (PyMuPDF)" if FITZ_AVAILABLE else "post-filtr (bbox)"
            logger.info(
                f"Marginesy: top={top_margin_crop}pt, bottom={bottom_margin_crop}pt, "
                f"left={left_margin_crop}pt, right={right_margin_crop}pt | "
                f"metoda: {crop_method}"
            )

        # ── GPU ───────────────────────────────────────────────────
        self._device = self._detect_device(use_gpu)

        accelerator = AcceleratorOptions(
            num_threads=num_threads,
            device=(
                AcceleratorDevice.CUDA
                if self._device == "cuda"
                else AcceleratorDevice.CPU
            ),
        )

        # ── Tabele ────────────────────────────────────────────────
        table_structure = TableStructureOptions(
            mode=(
                TableFormerMode.ACCURATE
                if table_mode == "accurate"
                else TableFormerMode.FAST
            ),
        )

        # ── OCR ───────────────────────────────────────────────────
        if ocr_languages is None:
            ocr_languages = ["pl", "en"]

        pipeline_options = PdfPipelineOptions(
            do_ocr=do_ocr,
            do_table_structure=True,
            table_structure_options=table_structure,
            accelerator_options=accelerator,
        )

        if do_ocr:
            pipeline_options.ocr_options = EasyOcrOptions(lang=ocr_languages)

        # ── Konwerter ─────────────────────────────────────────────
        logger.info("Ładowanie modeli Docling...")

        self.converter = DocumentConverter(
            format_options={
                InputFormat.PDF: PdfFormatOption(
                    pipeline_options=pipeline_options,
                )
            }
        )

        self._do_ocr = do_ocr
        self._table_mode = table_mode

        logger.info(
            f"DoclingPdfParser gotowy | device={self._device} | "
            f"OCR={do_ocr} ({ocr_languages}) | tabele={table_mode}"
        )

    # ══════════════════════════════════════════════════════════════
    # INTERFEJS PUBLICZNY
    # ══════════════════════════════════════════════════════════════

    def parse(
        self,
        file_source: Union[str, io.BytesIO, bytes],
        **kwargs,
    ) -> List[Document]:
        """
        Przetwarza PDF → lista Document (Markdown, 1 strona = 1 Document).

        Kwargs:
            full_document (bool): Cały dokument jako jeden Document.
                                  Domyślnie False.
        """
        full_document = kwargs.get("full_document", False)
        source_name = self._get_source_name(file_source)

        try:
            # ── 1. PRE-CROP marginesów (PyMuPDF) ─────────────────
            original_page_dims = None

            if self._margins_enabled and FITZ_AVAILABLE:
                logger.info(f"Pre-crop marginesów: {source_name}")
                cropped_stream, original_page_dims = self._precrop_pdf(file_source)
                conv_source = self._prepare_source(cropped_stream)
            else:
                conv_source = self._prepare_source(file_source)

            # ── 2. Konwersja Docling (GPU) ────────────────────────
            logger.info(f"Konwersja Docling: {source_name}")
            result = self.converter.convert(conv_source)
            doc = result.document
            logger.info(f"Konwersja zakończona: {source_name}")

            # ── 3. Budowanie dokumentów ───────────────────────────
            # Post-filtr bbox tylko gdy fitz niedostępny a marginesy włączone
            use_postfilter = self._margins_enabled and not FITZ_AVAILABLE

            if full_document:
                documents = self._build_full_document(doc, source_name)
            else:
                documents = self._build_page_documents(
                    doc,
                    source_name,
                    postfilter_margins=use_postfilter,
                )

            # ── 4. Uzupełnienie metadanych o oryginalne wymiary ──
            if original_page_dims:
                for d in documents:
                    page_no = d.metadata.get("page_number", 1)
                    if page_no in original_page_dims:
                        dims = original_page_dims[page_no]
                        d.metadata["original_page_width_pt"] = dims[0]
                        d.metadata["original_page_height_pt"] = dims[1]
                    d.metadata["margin_top_pt"] = self._top_margin
                    d.metadata["margin_bottom_pt"] = self._bottom_margin

            # ── 5. Cleanup GPU ────────────────────────────────────
            self._cleanup_gpu()

            logger.info(f"Wynik: {len(documents)} dokumentów z '{source_name}'")
            return documents

        except Exception as e:
            logger.error(f"Błąd Docling ({source_name}): {e}", exc_info=True)
            self._cleanup_gpu()
            return []

    def diagnostics(self) -> Dict[str, str]:
        """Informacje diagnostyczne."""


        info = {
            "device": self._device,
            "ocr": str(self._do_ocr),
            "table_mode": self._table_mode,
            "margins_enabled": str(self._margins_enabled),
            "margin_top_pt": str(self._top_margin),
            "margin_bottom_pt": str(self._bottom_margin),
            "margin_left_pt": str(self._left_margin),
            "margin_right_pt": str(self._right_margin),
            "crop_method": "pre-crop (PyMuPDF)" if FITZ_AVAILABLE else "post-filtr (bbox)",
            "torch_version": torch.__version__,
            "cuda_available": str(torch.cuda.is_available()),
        }

        if torch.cuda.is_available():
            info["gpu_name"] = torch.cuda.get_device_name(0)
            info["gpu_vram_gb"] = (
                f"{torch.cuda.get_device_properties(0).total_memory / 1024**3:.1f}"
            )

        return info

    # ══════════════════════════════════════════════════════════════
    # WARSTWA 1: PRE-CROP (PyMuPDF cropbox)
    # ══════════════════════════════════════════════════════════════

    def _precrop_pdf(
        self, file_source: Union[str, io.BytesIO, bytes]
    ) -> Tuple[io.BytesIO, Dict[int, Tuple[float, float]]]:
        """
        Fizyczne przycięcie marginesów za pomocą PyMuPDF cropbox.

        Docling NIGDY nie zobaczy treści w marginesach — nie przetworzy
        ich, nie zmarnuje na nie compute GPU.

        Returns:
            (cropped_pdf_stream, original_page_dimensions)
            original_page_dimensions: {page_no: (width, height)}
        """
        if isinstance(file_source, str):
            pdf_doc = fitz.Document(file_source)
        elif isinstance(file_source, bytes):
            pdf_doc = fitz.Document(stream=file_source, filetype="pdf")
        elif isinstance(file_source, io.BytesIO):
            file_source.seek(0)
            pdf_doc = fitz.Document(stream=file_source.read(), filetype="pdf")
        else:
            raise ValueError(f"Nieobsługiwany typ: {type(file_source)}")

        original_dims: Dict[int, Tuple[float, float]] = {}
        pages_cropped = 0

        for page_idx, page in enumerate(pdf_doc):
            rect = page.rect  # Oryginalne wymiary (x0, y0, x1, y1)

            # Zapisz oryginalne wymiary
            original_dims[page_idx + 1] = (rect.width, rect.height)

            # Oblicz nowy cropbox z walidacją
            new_x0 = rect.x0 + self._left_margin
            new_y0 = rect.y0 + self._top_margin
            new_x1 = rect.x1 - self._right_margin
            new_y1 = rect.y1 - self._bottom_margin

            # Walidacja: sprawdź czy po obcięciu zostaje sensowna powierzchnia
            remaining_width = new_x1 - new_x0
            remaining_height = new_y1 - new_y0

            if remaining_width < 100 or remaining_height < 100:
                logger.warning(
                    f"Strona {page_idx + 1}: marginesy zbyt duże "
                    f"(zostałoby {remaining_width:.0f}×{remaining_height:.0f} pt). "
                    f"Pomijam cropowanie tej strony."
                )
                continue

            new_rect = fitz.Rect(new_x0, new_y0, new_x1, new_y1)
            page.set_cropbox(new_rect)
            pages_cropped += 1

        logger.info(
            f"Pre-crop: przycięto {pages_cropped}/{len(pdf_doc)} stron "
            f"(top={self._top_margin}pt, bottom={self._bottom_margin}pt, "
            f"left={self._left_margin}pt, right={self._right_margin}pt)"
        )

        # Zapisz przycięty PDF do pamięci
        output = io.BytesIO()
        pdf_doc.save(output)
        pdf_doc.close()
        output.seek(0)

        return output, original_dims

    # ══════════════════════════════════════════════════════════════
    # WARSTWA 3: POST-FILTER (provenance bounding box)
    # Fallback gdy PyMuPDF niedostępny
    # ══════════════════════════════════════════════════════════════

    def _is_in_margin(
        self, item, page_height: float, page_width: float
    ) -> bool:
        """
        Sprawdza czy element znajduje się w strefie marginesu
        na podstawie jego bounding box z provenance.

        Obsługuje oba systemy współrzędnych Docling:
        - TOPLEFT:    (0,0) w lewym górnym rogu
        - BOTTOMLEFT: (0,0) w lewym dolnym rogu
        """
        if not hasattr(item, "prov") or not item.prov:
            return False

        try:
            bbox = item.prov[0].bbox

            # Odczytaj system współrzędnych
            coord_origin = getattr(bbox, "coord_origin", None)
            origin_value = (
                coord_origin.value
                if hasattr(coord_origin, "value")
                else str(coord_origin)
            )
            is_topleft = origin_value in ("TOPLEFT", "topleft", None)

            if is_topleft:
                # TOPLEFT: t mały = góra strony, b duży = dół strony
                #   bbox.t = odległość od góry do górnej krawędzi elementu
                #   bbox.b = odległość od góry do dolnej krawędzi elementu
                if self._top_margin > 0 and bbox.b <= self._top_margin:
                    return True  # Cały element w górnym marginesie
                if self._bottom_margin > 0 and bbox.t >= page_height - self._bottom_margin:
                    return True  # Cały element w dolnym marginesie
                if self._left_margin > 0 and bbox.r <= self._left_margin:
                    return True
                if self._right_margin > 0 and bbox.l >= page_width - self._right_margin:
                    return True
            else:
                # BOTTOMLEFT: b mały = dół strony, t duży = góra strony
                if self._bottom_margin > 0 and bbox.t <= self._bottom_margin:
                    return True  # Element w dolnym marginesie
                if self._top_margin > 0 and bbox.b >= page_height - self._top_margin:
                    return True  # Element w górnym marginesie
                if self._left_margin > 0 and bbox.r <= self._left_margin:
                    return True
                if self._right_margin > 0 and bbox.l >= page_width - self._right_margin:
                    return True

        except Exception as e:
            logger.debug(f"Błąd sprawdzania marginesu bbox: {e}")
            return False

        return False

    def _get_page_dimensions(self, doc) -> Dict[int, Tuple[float, float]]:
        """
        Pobiera wymiary stron z dokumentu Docling.

        Returns:
            {page_no: (width, height)}
        """
        dims: Dict[int, Tuple[float, float]] = {}

        if hasattr(doc, "pages"):
            for page_no, page_item in doc.pages.items():
                if hasattr(page_item, "size") and page_item.size:
                    dims[page_no] = (page_item.size.width, page_item.size.height)

        return dims

    # ══════════════════════════════════════════════════════════════
    # BUDOWANIE DOKUMENTÓW
    # ══════════════════════════════════════════════════════════════

    def _build_page_documents(
        self,
        doc,
        source_name: str,
        postfilter_margins: bool = False,
    ) -> List[Document]:
        """
        Buduje listę Document z podziałem na strony.

        Trójwarstwowe filtrowanie:
        1. SKIP_LABELS (semantyczne — page_header / page_footer)
        2. Pre-crop (jeśli zastosowany wcześniej — elementy już usunięte)
        3. Post-filter bbox (jeśli postfilter_margins=True)
        """
        page_contents: Dict[int, List[str]] = defaultdict(list)

        # Wymiary stron (do post-filtra)
        page_dims = self._get_page_dimensions(doc) if postfilter_margins else {}

        skipped_semantic = 0
        skipped_margin = 0
        total_elements = 0

        for item, level in doc.iterate_items():
            total_elements += 1
            label = getattr(item, "label", None)
            label_value = label.value if hasattr(label, "value") else str(label)

            # ── Warstwa 2: Filtr semantyczny (SKIP_LABELS) ───────
            if label_value in self.SKIP_LABELS:
                skipped_semantic += 1
                continue

            # Numer strony
            page_no = self._get_page_number(item)

            # ── Warstwa 3: Post-filtr marginesów (bbox) ──────────
            if postfilter_margins and page_no in page_dims:
                pw, ph = page_dims[page_no]
                if self._is_in_margin(item, page_height=ph, page_width=pw):
                    skipped_margin += 1
                    continue

            # Konwersja na Markdown
            md_fragment = self._item_to_markdown(item, level)
            if md_fragment:
                page_contents[page_no].append(md_fragment)

        # Logowanie statystyk filtrowania
        if skipped_semantic or skipped_margin:
            logger.info(
                f"Filtrowanie '{source_name}': "
                f"{total_elements} elementów, "
                f"pominięto {skipped_semantic} semantycznie + "
                f"{skipped_margin} marginesem"
            )

        # ── Fallbacki ─────────────────────────────────────────────
        if not page_contents:
            logger.warning(f"Brak elementów w '{source_name}' → fallback export_to_markdown()")
            return self._build_full_document(doc, source_name)

        if list(page_contents.keys()) == [0]:
            logger.warning(f"Brak provenance stron w '{source_name}' → jeden Document")
            return self._build_full_document(doc, source_name)

        # ── Budowanie obiektów Document ───────────────────────────
        documents = []
        total_pages = max(page_contents.keys()) if page_contents else 0

        for page_no in sorted(page_contents.keys()):
            if page_no <= 0:
                continue

            content = "\n\n".join(page_contents[page_no]).strip()
            if not content:
                continue

            documents.append(
                Document(
                    page_content=content,
                    metadata={
                        "page_number": page_no,
                        "total_pages": total_pages,
                        "source": source_name,
                        "parser": "docling",
                    },
                )
            )

        return documents

    def _build_full_document(self, doc, source_name: str) -> List[Document]:
        """Cały dokument jako jeden Document (natywny export Docling)."""
        try:
            full_md = doc.export_to_markdown().strip()
        except Exception as e:
            logger.error(f"export_to_markdown() failed: {e}")
            return []

        if not full_md:
            return []

        total_pages = len(doc.pages) if hasattr(doc, "pages") else 1

        return [
            Document(
                page_content=full_md,
                metadata={
                    "page_number": 1,
                    "total_pages": total_pages,
                    "source": source_name,
                    "parser": "docling",
                    "mode": "full_document",
                },
            )
        ]

    # ══════════════════════════════════════════════════════════════
    # METODY POMOCNICZE
    # ══════════════════════════════════════════════════════════════

    @staticmethod
    def _detect_device(use_gpu: bool) -> str:
        if not use_gpu:
            logger.info("GPU wyłączone → CPU")
            return "cpu"
        try:
            import torch

            if torch.cuda.is_available():
                name = torch.cuda.get_device_name(0)
                vram = torch.cuda.get_device_properties(0).total_memory / 1024**3
                logger.info(f"GPU: {name} ({vram:.1f} GB VRAM)")
                return "cuda"
            elif hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
                logger.info("Apple Silicon GPU (MPS)")
                return "mps"
            else:
                logger.warning("CUDA/MPS niedostępne → CPU")
                return "cpu"
        except ImportError:
            logger.warning("PyTorch nie zainstalowany → CPU")
            return "cpu"

    @staticmethod
    def _get_source_name(file_source: Union[str, io.BytesIO, bytes]) -> str:
        if isinstance(file_source, str):
            return os.path.basename(file_source)
        return "strumień pamięci (S3/RAM)"

    @staticmethod
    def _prepare_source(file_source: Union[str, io.BytesIO, bytes]):

        if isinstance(file_source, str):
            if not os.path.exists(file_source):
                raise FileNotFoundError(f"Plik nie istnieje: {file_source}")
            return file_source

        if isinstance(file_source, bytes):
            return DocumentStream(name="document.pdf", stream=io.BytesIO(file_source))

        if isinstance(file_source, io.BytesIO):
            file_source.seek(0)
            return DocumentStream(name="document.pdf", stream=file_source)

        raise ValueError(f"Nieobsługiwany typ: {type(file_source)}")

    @staticmethod
    def _get_page_number(item) -> int:
        if hasattr(item, "prov") and item.prov:
            prov = item.prov[0]
            if hasattr(prov, "page_no"):
                return prov.page_no
        return 0

    @staticmethod
    def _item_to_markdown(item, level: int) -> Optional[str]:
        label = getattr(item, "label", None)
        label_value = label.value if hasattr(label, "value") else str(label)

        if label_value == "section_header":
            text = getattr(item, "text", "")
            if not text:
                return None
            heading_level = min(max(getattr(item, "level", level + 1), 1), 6)
            return f"{'#' * heading_level} {text}"

        if label_value == "title":
            text = getattr(item, "text", "")
            return f"# {text}" if text else None

        if label_value == "table":
            try:
                if hasattr(item, "data") and item.data is not None:
                    return item.data.export_to_markdown()
                if hasattr(item, "export_to_markdown"):
                    return item.export_to_markdown()
                return getattr(item, "text", None)
            except Exception:
                return getattr(item, "text", None)

        if label_value == "list_item":
            text = getattr(item, "text", "")
            return f"- {text}" if text else None

        if label_value == "code":
            text = getattr(item, "text", "")
            return f"```\n{text}\n```" if text else None

        if label_value == "formula":
            text = getattr(item, "text", "")
            return f"$$\n{text}\n$$" if text else None

        if label_value == "caption":
            text = getattr(item, "text", "")
            return f"*{text}*" if text else None

        if label_value == "footnote":
            text = getattr(item, "text", "")
            return f"> {text}" if text else None

        text = getattr(item, "text", None)
        if text and text.strip():
            return text.strip()

        return None

    @staticmethod
    def _cleanup_gpu():
        try:
            import torch

            if torch.cuda.is_available():
                torch.cuda.empty_cache()
        except ImportError:
            pass