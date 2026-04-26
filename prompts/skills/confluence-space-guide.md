---
name: confluence-space-guide
description: Use this skill when the user asks to find, read, compare, summarize, draft, update, or organize content in Confluence across multiple spaces, especially when the correct space is ambiguous or the answer must be grounded in page metadata, hierarchy, labels, comments, views, or attachments.
compatibility: Requires MCP Atlassian Confluence tools such as confluence_search, confluence_get_page, confluence_get_page_children, confluence_get_page_history, confluence_get_page_diff, confluence_get_comments, confluence_get_labels, confluence_get_page_views, and optional write tools.
metadata:
  owner: "{{ORG_NAME}}"
  default_spaces: "{{DEFAULT_CONFLUENCE_SPACES}}"
  preferred_language: "pl"
  content_language_fallback: "en"
  write_mode: "{{WRITE_MODE}}"
  search_mode: "space-first"
---

# Confluence Space Guide

## Kiedy użyć tego skilla
Użyj tego skilla, gdy zadanie dotyczy:
- odnalezienia właściwej strony w wielu przestrzeniach,
- streszczenia lub porównania dokumentacji,
- znalezienia strony źródłowej dla wymagania, decyzji, procedury lub architektury,
- sprawdzenia aktualności treści,
- przygotowania draftu nowej strony albo aktualizacji istniejącej.

## Konfiguracja i personalizacja
Traktuj `{{DEFAULT_CONFLUENCE_SPACES}}` jako listę przestrzeni pierwszego wyboru.
Jeżeli użytkownik poda nazwę zespołu, produktu, domeny albo skrót projektu, najpierw mapuj to
na jedną z tych przestrzeni.

Możesz utrzymywać własny słownik routingu, np.:
- PAY -> PAYMENTS, OPS-PAY, SETTLEMENT
- ARCH -> ARCH, ADR, PLATFORM
- AML -> RISK, COMPLIANCE, FRAUD

Jeśli organizacja ma strony root dla zespołów, utrzymuj dodatkowo:
- `{{SPACE_ROOT_PAGE_IDS}}`
- `{{SPACE_PRIORITY_RULES}}`
- `{{TITLE_PREFIX_HINTS}}`

## Procedura pracy
1. Jeżeli użytkownik podał `page_id`, pobierz stronę bezpośrednio.
2. Jeżeli użytkownik podał dokładny tytuł i znasz `space_key`, użyj odczytu bezpośredniego.
3. Jeżeli nie znasz strony:
   - zacznij od wyszukania w skonfigurowanych przestrzeniach,
   - jeżeli użytkownik podał słowa kluczowe biznesowe, zacznij od prostego text search,
   - jeżeli użytkownik podał precyzyjne ograniczenia (space, label, parent page, czas), użyj CQL.
4. Gdy znajdziesz kandydata:
   - pobierz stronę z `include_metadata=true`,
   - domyślnie użyj `convert_to_markdown=true`,
   - użyj raw HTML tylko wtedy, gdy makra lub specjalne znaczniki są istotne dla pytania.
5. Gdy ważna jest struktura:
   - pobierz children strony,
   - w razie potrzeby pobierz historię i diff wersji.
6. Gdy ważna jest kontekstowość:
   - sprawdź labels,
   - sprawdź comments,
   - sprawdź page views dla oceny użycia lub "staleness".
7. Gdy strona odwołuje się do plików:
   - pobierz listę attachments,
   - dopiero potem decyduj, czy trzeba je analizować.
8. Przed każdą operacją zapisu:
   - odczytaj aktualną stronę,
   - podsumuj proponowaną zmianę,
   - poproś użytkownika o zgodę, jeśli `write_mode` nie pozwala na zapis bez potwierdzenia.

## Jak pisać odpowiedzi
W odpowiedzi zawsze podawaj:
- tytuł strony,
- przestrzeń,
- dlaczego ta strona jest właściwa,
- najważniejsze ustalenia,
- poziom pewności,
- pytania otwarte, jeśli nadal istnieje niejednoznaczność.

Jeśli istnieje kilka podobnych stron, nie wybieraj arbitralnie.
Zamiast tego pokaż 2–3 najlepsze kandydaty z krótkim uzasadnieniem.

## Wzorce CQL
Preferowane wzorce:
- `type = page AND space IN ("{{DEFAULT_CONFLUENCE_SPACES}}") AND text ~ "..." ORDER BY lastModified DESC`
- `type = page AND label = "..." ORDER BY title ASC`
- `ancestor = "PARENT_ID" AND type = page ORDER BY title ASC`
- `space = "SPACE" AND title ~ "..." ORDER BY lastModified DESC`

## Gotchas
- Nie zakładaj, że najnowsza strona jest najlepsza; starsza ADR może nadal być obowiązująca.
- Nie zakładaj, że podobne tytuły oznaczają duplikaty; mogą to być strony dla różnych zespołów.
- Jeśli widzisz konflikt między tytułem strony a treścią, zaufaj treści i historii wersji bardziej niż samemu tytułowi.
- Jeśli użytkownik chce "zaktualizować dokumentację", ale nie podał strony, nie twórz nowej strony automatycznie.
  Najpierw znajdź istniejący kandydat do aktualizacji.
