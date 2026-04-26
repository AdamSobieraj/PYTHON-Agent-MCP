---
name: jira-project-guide
description: Use this skill when the user asks to find, analyze, refine, create, update, transition, comment on, estimate, or organize Jira issues across multiple projects, boards, sprints, forms, or service desks, especially when project scope or custom fields are ambiguous.
compatibility: Requires MCP Atlassian Jira tools such as jira_get_all_projects, jira_search, jira_get_issue, jira_search_fields, jira_get_field_options, jira_get_transitions, jira_transition_issue, jira_get_agile_boards, jira_get_sprints_from_board, jira_get_sprint_issues, jira_add_comment, jira_add_worklog, jira_get_issue_sla, and related optional write tools.
metadata:
  owner: "{{ORG_NAME}}"
  default_projects: "{{DEFAULT_JIRA_PROJECTS}}"
  preferred_language: "pl"
  content_language_fallback: "en"
  write_mode: "{{WRITE_MODE}}"
  project_mode: "project-first"
---

# Jira Project Guide

## Kiedy użyć tego skilla
Użyj tego skilla, gdy zadanie dotyczy:
- znalezienia ticketów, epików, bugów, change requestów lub incydentów,
- analizy statusów, właścicieli, priorytetów i zależności,
- backlogu, sprintów, boardów i planowania prac,
- comments, worklogs, forms, SLA, development info,
- przygotowania draftu zmian w Jira lub wykonania zmian po akceptacji.

## Konfiguracja i personalizacja
Traktuj `{{DEFAULT_JIRA_PROJECTS}}` jako listę projektów pierwszego wyboru.
Utrzymuj mapowanie skrótów domenowych produktu/zespołu na projekty, np.:
- PAY -> PAY, INST, SETTLE
- AML -> RISK, FRAUD
- CORE -> CORE, ARCH, PLATFORM

Jeżeli masz znane boardy lub ważne issue types, zachowuj:
- `{{DEFAULT_BOARD_NAMES}}`
- `{{IMPORTANT_ISSUE_TYPES}}`
- `{{CUSTOM_FIELD_HINTS}}`
- `{{TRANSITION_POLICY}}`

## Procedura pracy
1. Ustal projekt.
   - Jeżeli użytkownik podał issue key, użyj go bezpośrednio.
   - Jeżeli projekt nie jest pewny, sprawdź listę projektów albo użyj wyszukiwania ograniczonego do domyślnych projektów.
2. Do wyszukiwania używaj JQL z `ORDER BY`.
3. Domyślnie pobieraj minimalny zestaw pól:
   - `summary,status,assignee,priority,issuetype,updated`
   - rozszerzaj tylko wtedy, gdy pytanie tego wymaga.
4. Gdy potrzebujesz custom field:
   - najpierw odkryj field ID przez search fields,
   - potem pobierz allowed options, jeśli pole jest wybieralne.
5. Gdy pytanie dotyczy statusów i zmian:
   - pobierz issue,
   - jeśli ma dojść do transition, najpierw pobierz transitions.
6. Gdy pytanie dotyczy sprintów lub backlogu:
   - ustal board,
   - pobierz sprinty,
   - pobierz sprint issues lub board issues.
7. Gdy pytanie dotyczy operations / support:
   - użyj worklogów, comments, SLA, issue dates, service desk queue albo forms.
8. Gdy pytanie dotyczy powiązań:
   - sprawdź links, epic linkage, versions, components, remote links.
9. Przed każdą operacją zapisu:
   - przedstaw plan zmiany,
   - pokaż dokładne pole/pola, które chcesz zmienić,
   - uzyskaj akceptację, jeśli write mode tego wymaga.

## Jak pisać odpowiedzi
W odpowiedzi zawsze podawaj:
- issue key albo zakres issue keys,
- projekt,
- status i właściciela, jeśli są istotne,
- istotny kontekst z komentarzy lub historii zmian,
- proponowaną akcję albo pytania otwarte.

Jeżeli użytkownik opisuje problem, ale nie zna issue key:
- najpierw zaproponuj 2–5 najlepszych kandydatów,
- nie wybieraj jednego biletu arbitralnie.

## Wzorce JQL
Preferowane wzorce:
- `project IN ({{DEFAULT_JIRA_PROJECTS}}) AND text ~ "..." ORDER BY updated DESC`
- `project = PROJ AND status = "In Progress" ORDER BY updated DESC`
- `project = PROJ AND assignee = currentUser() AND resolution = EMPTY ORDER BY priority DESC`
- `project = PROJ AND sprint IS EMPTY AND status = "Open" ORDER BY priority DESC, created ASC`

## Custom fields
Nigdy nie zgaduj `customfield_XXXXX`.
Najpierw odkryj field ID. Jeśli to pole ma listę wartości, pobierz opcje.
Jeśli kontekst zależy od issue type lub konkretnego projektu, zawęź to jawnie.

## Operacje zapisu
Dla create/update/transition/comment/worklog/link/version/form update:
- pokaż użytkownikowi plan,
- pokaż dokładną treść payloadu biznesowego,
- po akceptacji wykonaj write,
- po write zwróć wynik i co dokładnie się zmieniło.

## Gotchas
- Nie zakładaj, że ten sam workflow istnieje we wszystkich projektach.
- Nie zakładaj, że pole "Story Points" ma ten sam field ID wszędzie.
- Nie zakładaj, że transition name wystarczy; system może wymagać konkretnego transition ID.
- Jeśli kilka projektów ma podobny zakres, pokaż użytkownikowi kandydatów zamiast zgadywać.
