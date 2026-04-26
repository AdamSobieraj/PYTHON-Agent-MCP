---
name: vector-rag-research
description: Use this skill when the user asks a knowledge question that should be grounded in a vector knowledge base retrieval, especially when you need supporting passages, metadata, document provenance, or cross-document evidence before answering or deciding whether to fetch the source document.
compatibility: Requires a retrieval tool equivalent to run_generic_rag(query, collection_name, top_k) that returns chunks with metadata and relevance scores.
metadata:
  owner: "{{ORG_NAME}}"
  default_collections: "{{DEFAULT_RAG_COLLECTIONS}}"
  preferred_language: "pl"
  content_language_fallback: "en"
  top_k_default: "{{TOP_K_DEFAULT}}"
  retrieval_mode: "evidence-first"
---

# Vector RAG Research

## Kiedy użyć tego skilla
Użyj tego skilla, gdy pytanie:
- wymaga odpowiedzi opartej o bazę wiedzy,
- dotyczy pojęć, procedur, standardów, dokumentacji lub decyzji zapisanych w dokumentach,
- wymaga potwierdzenia źródłem zamiast odpowiedzi z pamięci modelu,
- wymaga znalezienia właściwego dokumentu przed dalszą analizą.

## Założenie operacyjne
Narzędzie retrieval NIE odpowiada za Ciebie.
Zwraca jedynie fragmenty tekstu i metadane. Twoim zadaniem jest:
- ocenić, czy fragment rzeczywiście odpowiada na pytanie,
- połączyć fragmenty z tego samego dokumentu,
- wykryć konflikt albo brak dowodu,
- zdecydować, czy trzeba pobrać więcej kontekstu z S3.

## Procedura pracy
1. Ustal najbardziej prawdopodobną kolekcję:
   - najpierw `{{DEFAULT_RAG_COLLECTIONS}}`,
   - jeśli domena jest znana, wybierz kolekcję domenową,
   - jeśli domena nie jest znana, zaczynaj od kolekcji ogólnej.
2. Zbuduj query retrievalowe:
   - zachowaj słowa domenowe z pytania,
   - dodaj synonimy techniczne, jeśli to pomaga,
   - jeśli pytanie jest po polsku, ale dokumentacja jest często po angielsku, zbuduj query,
     które zachowa kluczowe terminy angielskie.
3. Zacznij od umiarkowanego `top_k`:
   - zwykle 5–8,
   - zwiększ tylko wtedy, gdy pierwsze wyniki są za płytkie albo niespójne.
4. Po otrzymaniu wyników:
   - grupuj po `s3_uri`, `title`, `url` lub innym stabilnym identyfikatorze źródła,
   - traktuj relevance jako ranking pomocniczy,
   - porównaj, czy kilka fragmentów z tego samego dokumentu nie daje mocniejszego dowodu.
5. Jeśli fragment jest obiecujący, ale urwany:
   - użyj skilla S3 Source Reader.
6. Jeżeli kilka dokumentów jest sprzecznych:
   - pokaż konflikt,
   - wskaż, które źródło wygląda na bardziej autorytatywne,
   - nie rozstrzygaj arbitralnie bez dowodu.
7. Jeżeli nie ma wystarczającego dowodu:
   - powiedz to wprost,
   - zaproponuj dalszą ścieżkę: większe `top_k`, inną kolekcję, albo pobranie dokumentu.

## Jak używać metadanych
Traktuj następujące pola jako najważniejsze:
- `title` / `document_title`
- `s3_uri`
- `url`
- `domain`
- `range_start` / `Zakres_od`
- `range_end` / `Zakres_do`
- `type`
- `tags`
- `chunk_id`
- `relevance`

Jeśli brak części pól, nadal odpowiadaj, ale jawnie zaznacz niższą jakość provenance.

## Jak pisać odpowiedzi
W odpowiedzi zawsze pokazuj:
- krótką odpowiedź na pytanie,
- z jakiego dokumentu wnioskujesz,
- czy odpowiedź opiera się na jednym fragmencie, wielu fragmentach czy wielu dokumentach,
- czy dowód jest wystarczający,
- czy warto pobrać szerszy kontekst z S3.

## Gotchas
- Wysoki score nie oznacza, że fragment rozstrzyga pytanie.
- Fragment może być poprawny, ale nieaktualny lub dotyczyć innego wariantu procesu.
- Jeśli title i treść są niespójne, ufaj treści bardziej niż nazwie pliku.
- Jeśli dokument jest publiczny, nie zakładaj, że opisuje lokalną implementację organizacji.
