import sys
import wikipedia


def run_wikipedia_search(query: str) -> str:
    """
    ### SEARCHING IN WIKIPEDIA

    Used to fetch encyclopedia definitions.
    Works in this mode: Search -> Pick the best one -> Fetch the content.
    """
    print(f"[Wikipedia] Szukam hasła: '{query}'", file=sys.stderr)

    # Set the Wikipedia language (can be changed to 'pl')
    wikipedia.set_lang("en")

    try:
        # 1. Search for the list of matching articles
        search_results = wikipedia.search(query)

        if not search_results:
            return "Nie znaleziono artykułów w Wikipedii na ten temat."

        # 2. Fetch the content of the first (most relevant) result
        # auto_suggest=False: disabled so the library doesn't guess "too much"
        page_title = search_results[0]
        page = wikipedia.page(page_title, auto_suggest=False)

        # 3. Content truncation
        # We only take the first 1500 characters. The LLM doesn't need the whole article,
        # usually the lead is enough for a definition.
        summary = page.content[:1500]

        return f"--- WIKIPEDIA: {page.title} ---\n{summary}\n...(tekst przycięty ze względu na limit)..."

    except wikipedia.exceptions.DisambiguationError as e:
        # Handling the situation: "Java" -> (Island, Coffee, Programming language?)
        options = ", ".join(e.options[:5])
        return f"Hasło '{query}' jest niejednoznaczne. Czy chodziło Ci o: {options}?"

    except wikipedia.exceptions.PageError:
        return f"Strona o tytule '{query}' nie istnieje, mimo że wyszukiwarka ją zasugerowała."

    except Exception as e:
        return f"Nieoczekiwany błąd Wikipedii: {str(e)}"