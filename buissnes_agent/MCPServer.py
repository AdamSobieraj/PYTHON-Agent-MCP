from __future__ import annotations

import sys

from pathlib import Path

try:
    from .mcp_server import main
except ImportError:
    current_dir = Path(__file__).resolve().parent
    parent_dir = current_dir.parent
    if str(parent_dir) not in sys.path:
        sys.path.insert(0, str(parent_dir))
    from buissnes_agent.mcp_server import main


if __name__ == "__main__":
    main()

# Prompty testowe
# RAG
# Wymień pola obowiązkowe w bloku Group Header dla komunikatu pacs.008 zgodnie ze specyfikacją CBPR+.
# Jaki jest maksymalny limit znaków dla pola EndToEndIdentification i czy dozwolone są w nim znaki specjalne?
# Wyjaśnij, czego dotyczy reguła walidacyjna VR00060 w kontekście komunikatu pacs.008.
# Czy blok 'Remittance Information' jest obowiązkowy w komunikacie camt.053 i jakie pod-pola zawiera w wersji 001.08?
# Wikipedia
# Kiedy powstała organizacja SWIFT i gdzie znajduje się jej główna siedziba?
# Confluence
# Jak wygląda nasza wewnętrzna procedura walidacji komunikatów płatniczych przed wysyłką?
# hybryda
# Co to jest komunikat camt.053 i jak go archiwizujemy w naszym systemie?

# nowe wytyczne
# nie przetważać xsd tylko podczas przetważania dokumentu pdf zrobic po tytułach
# xsd na serwerze i w metadanych link do nich
# chunking pliku dodawanego w chacie z tymczasowym bazą

# pdf czy do markdown czy nie

# teraz startowanie ingestion python main.py --profile prod --collection-name my_custom_collection_v2 --bucket mojsuperbucket

# docx do pdf

# in memory załadowanie tmp plik

# httpd i potem kong

# dynamicznie towrzone toole