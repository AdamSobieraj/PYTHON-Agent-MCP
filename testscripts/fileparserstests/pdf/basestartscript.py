import os
import sys
import time
import shutil

# Importujemy parsery z użyciem aliasów
from pdf_parser_pymupdf4llm import PdfParser as PyMuPdfParser
from pdf_parser_kreuzberg import PdfParser as KreuzbergParser
from pdf_parser_docling import PdfParser as DoclingParser


def run_parser_and_save(parser_name: str, parser_class, pdf_path: str, base_output_folder: str):
    """
    Funkcja uruchamia dany parser, mierzy czas i zapisuje wynik.
    Zwraca tuple: (czas_wykonania, liczba_elementów, liczba_znaków)
    """
    # 1. Utworzenie dedykowanego podfolderu dla parsera
    output_folder = os.path.join(base_output_folder, parser_name)
    os.makedirs(output_folder, exist_ok=True)

    print(f"\n[{parser_name}] Przetwarzanie pliku: {pdf_path}...")

    # 2. Inicjalizacja parsera i start pomiaru czasu
    parser = parser_class()
    start_time = time.time()

    # Wywołanie metody parse
    documents = parser.parse(pdf_path)

    # Koniec pomiaru czasu
    end_time = time.time()
    elapsed_time = end_time - start_time

    if not documents:
        print(f"[{parser_name}] Ostrzeżenie: Parsowanie zakończyło się pustym wynikiem.")
        return elapsed_time, 0, 0

    # Zabezpieczenie: jeśli parser nie zwraca listy, tylko pojedynczy obiekt
    if not isinstance(documents, (list, tuple)):
        documents = [documents]

    # 3. Ustalenie nazwy pliku wyjściowego
    base_name = os.path.basename(pdf_path)
    file_name_without_ext = os.path.splitext(base_name)[0]
    output_file_path = os.path.join(output_folder, f"{file_name_without_ext}.md")

    # 4. Zapisanie Markdowna do pliku i zliczanie znaków
    total_characters = 0

    print(f"[{parser_name}] Zapisywanie wyniku do: {output_file_path}")
    with open(output_file_path, "w", encoding="utf-8") as md_file:
        for doc in documents:
            # Próba wyciągnięcia numeru strony (zabezpieczone)
            page_num = doc.metadata.get("page_number", "?") if hasattr(doc, 'metadata') else "?"
            md_file.write(f"<!-- ELEMENT {page_num} -->\n")

            # Próba wyciągnięcia treści (zabezpieczone)
            content = doc.page_content if hasattr(doc, 'page_content') else str(doc)

            # Zliczamy wyekstrahowane znaki
            total_characters += len(content)

            md_file.write(content)
            md_file.write("\n\n---\n\n")

    print(
        f"[{parser_name}] Gotowe! Zapisano elementów: {len(documents)}, Znaków: {total_characters}. Czas: {elapsed_time:.2f} s.")

    # Zwracamy czas, liczbę elementów oraz długość tekstu do raportu
    return elapsed_time, len(documents), total_characters


def process_pdf_to_test_folders(pdf_path: str):
    base_output_folder = "output"

    # --- Czyszczenie poprzednich wyników ---
    if os.path.exists(base_output_folder):
        print(f"Czyszczenie poprzednich wyników (usuwanie folderu '{base_output_folder}')...")
        shutil.rmtree(base_output_folder)

    # Utworzenie świeżego folderu 'output'
    os.makedirs(base_output_folder, exist_ok=True)
    # -----------------------------------------------

    # Sprawdź, czy plik PDF istnieje
    if not os.path.exists(pdf_path):
        print(f"Błąd: Nie znaleziono pliku PDF pod ścieżką: {pdf_path}")
        return

    # Słownik z parserami, które chcemy przetestować
    parsers = {
        "pymupdf4llm": PyMuPdfParser,
        "kreuzberg": KreuzbergParser,
        "docling": DoclingParser
    }

    timing_results = []

    # Wykonanie przetwarzania dla każdego parsera w pętli
    for name, p_class in parsers.items():
        try:
            elapsed_time, elements_count, total_chars = run_parser_and_save(name, p_class, pdf_path, base_output_folder)
            timing_results.append({
                "parser": name,
                "time": elapsed_time,
                "elements": elements_count,
                "chars": total_chars
            })
        except Exception as e:
            print(f"[{name}] Wystąpił błąd podczas przetwarzania: {e}")

    # 5. Zapis raportu czasowego i statystyk
    base_name = os.path.basename(pdf_path)
    file_name_without_ext = os.path.splitext(base_name)[0]
    timing_file_path = os.path.join(base_output_folder, f"timing_{file_name_without_ext}.txt")

    print(f"\nZapisywanie raportu wydajnościowego do: {timing_file_path}")
    with open(timing_file_path, "w", encoding="utf-8") as t_file:
        t_file.write(f"Raport przetwarzania pliku: {pdf_path}\n")
        t_file.write("=" * 60 + "\n")

        for res in timing_results:
            t_file.write(f"Parser: {res['parser']}\n")
            t_file.write(f"Czas wykonania: {res['time']:.4f} sekund\n")
            t_file.write(f"Liczba zwróconych elementów (np. stron): {res['elements']}\n")
            t_file.write(f"Całkowita liczba wyciągniętych znaków: {res['chars']}\n")
            t_file.write("-" * 40 + "\n")

    print("Zakończono wszystkie zadania pomyślnie. Sprawdź folder 'output'.")


if __name__ == "__main__":
    # Obsługa argumentów z wiersza poleceń
    if len(sys.argv) > 1:
        target_pdf = sys.argv[1]
    else:
        target_pdf = "data/ISO_20022_Programme_UHB_SR2023_Edition.pdf"
        print(f"Nie podano pliku w argumencie. Używam domyślnego: {target_pdf}")

    process_pdf_to_test_folders(target_pdf)