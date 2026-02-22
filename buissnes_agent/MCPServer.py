import asyncio
import logging
import sys
import os
from fastmcp import FastMCP

from tools.tool_confluence import run_confluence_search
# IMPORTY LOGIKI NARZĘDZI
from tools.tool_iso_rag import run_generic_rag
from tools.tool_wikipedia import run_wikipedia_search

logging.basicConfig(level=logging.INFO, stream=sys.stderr)

# Wyciszenie logów bibliotek HTTP (zbyt gadatliwe)
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("httpcore").setLevel(logging.WARNING)

# Inicjalizacja instancji FastMCP (nazwa serwera widoczna dla klienta)
mcp = FastMCP("ISO20022 RAG Analyst Service")


# ==============================================================================
# DEFINICJA NARZĘDZI MCP (Tool Registration)
# ==============================================================================

@mcp.tool()
async def query_iso20022_business_knowledge_base(query: str) -> str:
    """
    Wyszukuje informacje w biznesowej bazie która wyjaśniają płatności ISO 20022 w praktyce — głównie SWIFT CBPR+ (co to jest, przepływy transgraniczne, struktura komunikatów, role/opłaty, podstawy nt. pacs.008/pacs.009, odrzucenie/zwrot z przykładami i przykładowymi komunikatami) oraz usługi Eurosystemu TARGET (adresowanie i uczestnictwo w T2/RTGS oraz koncepcje TIPS/SCT Inst, takie jak strony/rachunki, transfery płynności i opcje rozliczeń). Zawiera również przydatne elementy implementacji ISO 20022/XML (kardynalność/obowiązkowa vs. opcjonalna, reprezentacja waluty/kwoty, offsety UTC, LEI, zagadnienia dotyczące danych dłużnika/wierzyciela w stylu FATF16).
    Użyj tego narzędzia do pytań o:
    - Dochodzenia SWIFT CBPR+ (transgraniczne): „Czym jest CBPR+?”, które komunikaty są objęte zakresem, jak CBPR+ opisuje przepływy i przykładowe komunikaty.
    - Wykorzystanie pacs.008/pacs.009 i mechanizmy łańcucha płatności: np. logika routingu/rozliczeń SERIAL vs COVER, sposób przetwarzania przelewów bankowych, kiedy pacs.009 ADV jest bezpośredni, a nie przekazywany.
    - Wyjątki/wyniki w przepływach: pytania dotyczące zachowań odrzuceń/zwrotów i sposobu, w jaki te scenariusze są ujęte w przepływach CBPR+.
    - Role, adresowanie i „kto co wysyła do kogo” w łańcuchach wielobankowych: role statyczne vs dynamiczne, koncepcje danych punkt-punkt vs end-to-end, obsługa opłat (kto ponosi za co).
    - Usługi TARGET (T2) – pytania: jak kontekst RTGS/CLM wpływa na adresowanie, typy uczestnictwa i łańcuchy mieszane, w których odcinek T2 łączy się z odcinkiem CBPR+.
    - Pytania operacyjne dotyczące TIPS/SCT Inst: czym jest TIPS, zasady transferu płynności, strony/rachunki i konfiguracje opcji rozliczeniowych.
    - ISO 20022 XML „jak to przedstawić/zwalidować?”: formatowanie waluty i kwoty, przesunięcia UTC, wzorce XSD oraz interpretacja obowiązkowa i opcjonalna – przydatne podczas wdrażania/analizy komunikatów.
    """
    collection_name = os.getenv('ISO20022_BUSINESS_COLLECTION_NAME')
    # WAŻNE: asyncio.to_thread uruchamia funkcję synchroniczną (run_iso_rag) w osobnym wątku.
    # Zapobiega to blokowaniu pętli zdarzeń (Event Loop) serwera, gdy czekamy na bazę danych.
    return await asyncio.to_thread(run_generic_rag, query, collection_name)

@mcp.tool()
async def query_iso20022_technical_knowledge_base(query: str) -> str:
    """
    Wyszukuje informacje w technicznej bazie wiedzy  oficjalnych raportów definicji komunikatów (MDR) zgodnych z normą ISO 20022 w różnych obszarach (płatności, zarządzanie gotówką itp.). MDR w pełni opisują zbiór komunikatów – kontekst biznesowy i szczegółowe definicje komunikatów (a czasem także powiązane wytyczne dotyczące ich wykorzystania).
    Użyj tego narzędzia gdy:
    - potrzebujesz wiarygodnych odpowiedzi na poziomie specyfikacji
    - Cel komunikatu (lub zestawu komunikatów), jego zakres, podmioty/role i procesy biznesowe.
    - Dokładna struktura komunikatów ISO 20022: elementy, definicje i sposób formalnego opisu komunikatu w dokumentacji MDR.
    - Pytania międzydziedzinowe, w których musisz polegać na oficjalnych definicjach ISO 20022 (a nie na interpretacjach dostawców/blogów), np. porównanie pojęć dotyczących płatności, papierów wartościowych i sprawozdawczości regulacyjnej.
    """
    collection_name = os.getenv('ISO20022_TECHNICAL_COLLECTION_NAME')
    # WAŻNE: asyncio.to_thread uruchamia funkcję synchroniczną (run_iso_rag) w osobnym wątku.
    # Zapobiega to blokowaniu pętli zdarzeń (Event Loop) serwera, gdy czekamy na bazę danych.
    return await asyncio.to_thread(run_generic_rag, query, collection_name)

@mcp.tool()
async def query_iso20022_message_schemas_knowledge_base(query: str) -> str:
    """
    Wyszukuje informacje w technicznej bazie wiedzy ISO 20022 zawierającej głównie schematy XML (XSD) dla komunikatów ISO 20022. Służy do walidacji, generowania, analizy składniowej i mapowania ładunków komunikatów na poziomie składni/struktury.
    Użyj tego narzędzia do pytań o:
    - Walidacja lub debugowanie struktury komunikatu: „Dlaczego ten XML nie przechodzi walidacji?”, „Który element jest tu dozwolony?”, „Jakie jest prawidłowe zagnieżdżenie/kolejność/kardynalność zgodnie ze schematem?”
    - Tworzenie parserów/maperów/generatorów: generowanie kodu z XSD, budowanie reguł transformacji, mapowanie pól między wersjami/wariantami lub tworzenie przykładowych szkieletów danych zgodnych z ograniczeniami schematu.
    - Implementacje API/XML: gdy użytkownik potrzebuje reprezentacji XML zgodnej z semantyką ISO 20022 (i masz artefakty schematu XML w kolekcji) lub potrzebuje wskazówek opartych na metodach generowania schematu XML zgodnych z ISO 20022.
    """
    collection_name = os.getenv('ISO20022_MESSAGE_SCHEMAS_COLLECTION_NAME')
    # WAŻNE: asyncio.to_thread uruchamia funkcję synchroniczną (run_iso_rag) w osobnym wątku.
    # Zapobiega to blokowaniu pętli zdarzeń (Event Loop) serwera, gdy czekamy na bazę danych.
    return await asyncio.to_thread(run_generic_rag, query, collection_name)

@mcp.tool()
async def search_wikipedia_general(query: str) -> str:
    """
    Przeszukuje Wikipedię w celu znalezienia definicji ogólnych, historii, kodów krajów itp.
    Użyj tego narzędzia do pytań nietechnicznych:
    - Definicje biznesowe (np. "Co to jest IBAN?").
    - Informacje o organizacjach (SWIFT, FED, EBA).
    - Dane geograficzne i historyczne.
    """
    return await asyncio.to_thread(run_wikipedia_search, query)


# @mcp.tool()
# async def search_confluence_internal(query: str) -> str:
#     """
#     Przeszukuje wewnętrzną dokumentację firmy w Confluence.
#     Użyj tego narzędzia do pytań o:
#     - Procedury operacyjne ("Jak my to robimy?").
#     - Ustalenia projektowe i notatki ze spotkań.
#     - Specyfikę wdrożenia systemów w organizacji.
#     """
#     return await asyncio.to_thread(run_confluence_search, query)


# ==============================================================================
# URUCHOMIENIE SERWERA (Entry Point)
# ==============================================================================

if __name__ == "__main__":
    import argparse

    # 1. Konfiguracja argumentów linii poleceń (CLI Args)
    # Pozwala to na elastyczne uruchamianie serwera w różnych trybach architektury A2A.
    parser = argparse.ArgumentParser(description="Uruchamia serwer MCP dla Agenta ISO 20022")

    parser.add_argument("--transport", default="stdio", choices=["stdio", "sse",  "http"],
                        help="Tryb transportu: 'stdio' (lokalny pipe, domyślny) lub 'sse' (HTTP server)")
    parser.add_argument("--port", default=8000, type=int,
                        help="Port nasłuchiwania dla trybu SSE (domyślnie 8000)")
    parser.add_argument("--host", default="0.0.0.0",
                        help="Host nasłuchiwania dla trybu SSE (domyślnie wszystkie interfejsy)")

    # parse_known_args jest bezpieczniejsze niż parse_args, bo FastMCP może używać własnych flag
    args, _ = parser.parse_known_args()

    print(f"Starting ISO20022 RAG MCP Server in mode: {args.transport.upper()} {args.port} {args.host}...", file=sys.stderr)

    # 2. Wybór trybu uruchomienia
    if args.transport == "sse":
        # Tryb SSE: Serwer HTTP (np. dla komunikacji między kontenerami Docker)
        # Uruchomienie: python MCPServer.py --transport sse
        mcp.host = args.host
        mcp.port = args.port
        mcp.run(transport="sse")
    elif args.transport == "http":
        mcp.run(transport="http", host=args.host, port=args.port)
    else:
        # Tryb STDIO: Komunikacja przez standardowe wejście/wyjście.
        # Domyślny tryb dla klientów lokalnych (np. Claude Desktop App lub nasz testscripts.py)
        mcp.run(transport="stdio")


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