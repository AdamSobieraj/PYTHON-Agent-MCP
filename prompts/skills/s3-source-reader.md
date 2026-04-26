---
name: s3-source-reader
description: Use this skill when you already have an exact s3_uri from retrieval metadata and need either the full source document or a larger surrounding excerpt via byte range, especially for grounded analysis, traceability, and source verification.
compatibility: Requires document tools equivalent to download_text_response(bucket_name, object_key) and download_text_range(bucket_name, object_key, start_byte, end_byte).
metadata:
  owner: "{{ORG_NAME}}"
  preferred_language: "pl"
  content_language_fallback: "en"
  range_expansion_bytes: "{{RANGE_EXPANSION_BYTES}}"
  full_download_threshold_bytes: "{{FULL_DOWNLOAD_THRESHOLD_BYTES}}"
  fetch_strategy: "range-then-full"
---

# S3 Source Reader

## Kiedy użyć tego skilla
Użyj tego skilla, gdy:
- masz już `s3_uri` z retrieval metadata,
- potrzebujesz większego kontekstu niż sam chunk,
- chcesz potwierdzić strukturę dokumentu, sekcję, nagłówek albo źródłowy wording,
- chcesz zbudować odpowiedź opartą o pełen dokument, a nie tylko wycinek.

## Zasady podstawowe
- Zawsze używaj DOKŁADNEGO `s3_uri` ze źródła metadata.
- Preferuj range fetch, gdy potrzebujesz tylko lokalnego kontekstu wokół fragmentu.
- Preferuj full fetch, gdy:
  - musisz zrozumieć strukturę całego dokumentu,
  - analizujesz kilka fragmentów z tego samego pliku,
  - pytanie dotyczy spójności całego dokumentu,
  - zakresy są tak rozproszone, że kilka range fetches byłoby gorsze niż full read.

## Heurystyka wyboru
1. Jeśli masz pojedynczy chunk i pytanie dotyczy jednej tezy:
   - pobierz range zaczynając od `range_start`,
   - zakończ na `range_end`,
   - opcjonalnie rozszerz zakres o `{{RANGE_EXPANSION_BYTES}}` w obie strony.
2. Jeśli masz 2+ chunki z tego samego dokumentu i są blisko siebie:
   - scal je w jeden większy range.
3. Jeśli pobrany range urywa zdanie, tabelę lub nagłówek:
   - rozszerz range albo pobierz cały dokument.
4. Jeśli dokument jest krótki albo ma wyraźną strukturę markdown:
   - pełny odczyt często jest lepszy niż kilka range calls.

## Procedura pracy
1. Odczytaj `s3_uri`.
2. Ustal, czy potrzebny jest full fetch czy range fetch.
3. Po pobraniu treści:
   - zlokalizuj fragment źródłowy,
   - zidentyfikuj nagłówek, sekcję lub kontekst otaczający,
   - zanotuj, czy treść potwierdza lub osłabia wniosek z retrievalu.
4. W odpowiedzi zachowaj provenance:
   - `s3_uri`,
   - title / url jeśli znane,
   - zakres bajtów, jeżeli użyto range fetch.

## Jak pisać odpowiedzi
Wynik powinien zawierać:
- co zostało pobrane: full czy range,
- z jakiego źródła,
- jaki kontekst dodatkowy został odkryty,
- czy pierwotny chunk był reprezentatywny,
- czy potrzebny jest dalszy odczyt.

## Gotchas
- Range fetch może zacząć się lub skończyć w środku znaków, zdań, tabel lub bloków markdown.
- Nie zakładaj, że rozszerzenie `.md` oznacza mały plik.
- Jeśli kilka chunków z jednego dokumentu wskazuje różne sekcje, nie interpretuj ich bez sprawdzenia układu całego dokumentu.
