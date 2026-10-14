import os
import sys
from atlassian import Confluence
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

def _get_confluence_client():
    """Helper function for Atlassian Cloud authentication"""
    url = os.getenv("CONFLUENCE_URL")
    username = os.getenv("CONFLUENCE_USERNAME")
    token = os.getenv("CONFLUENCE_API_TOKEN")

    if not all([url, username, token]):
        return None

    return Confluence(
        url=url,
        username=username,
        password=token,  # In the cloud we pass the API token as the password
        cloud=True
    )


def run_confluence_search(query: str) -> str:
    """
    ### SEARCHING IN CONFLUENCE (Internal Knowledge Base)

    Uses CQL (Confluence Query Language) to find pages,
    then BeautifulSoup to clean the HTML content.
    """
    print(f"[Confluence] Szukam: '{query}'", file=sys.stderr)

    confluence = _get_confluence_client()
    if not confluence:
        return "Błąd konfiguracji: Brak zmiennych CONFLUENCE_* w pliku .env."

    try:
        # 1. Build the CQL query
        # title ~ "x" OR text ~ "x" -> search in the title or in the content
        # type = "page" -> ignore attachments, comments and blogposts
        cql = f'(title ~ "{query}" OR text ~ "{query}") AND type = "page"'

        # Fetch at most 3 results so we don't pollute the context
        results = confluence.cql(cql, limit=3)

        if not results.get("results"):
            return "Nie znaleziono żadnych dokumentów wewnętrznych pasujących do zapytania."

        final_output = []

        # 2. Iterate over the results and fetch the content
        for page in results["results"]:
            page_id = page["content"]["id"]
            page_title = page["content"]["title"]

            # Build the link to the page (for the user)
            base_url = os.getenv('CONFLUENCE_URL')
            webui = page['content']['_links']['webui']
            # Sometimes webui already contains /wiki, sometimes not - normalization:
            page_url = f"{base_url}/wiki{webui}" if not webui.startswith('/wiki') else f"{base_url}{webui}"

            # Fetch the full content (body.storage = Confluence's HTML format)
            full_page = confluence.get_page_by_id(page_id, expand='body.storage')
            raw_html = full_page['body']['storage']['value']

            # 3. HTML Parsing & Cleaning
            # The LLM prefers clean text over <div><span>...
            soup = BeautifulSoup(raw_html, "html.parser")
            text_content = soup.get_text(separator="\n").strip()

            # Length limit per page
            max_chars = int(os.getenv("CONFLUENCE_MAX_CHARS", 2000))
            if len(text_content) > max_chars:
                text_content = text_content[:max_chars] + "\n...(ucięto resztę strony)..."

            final_output.append(f"--- STRONA CONFLUENCE: {page_title} ---\nURL: {page_url}\nTREŚĆ:\n{text_content}\n")

        return "\n".join(final_output)

    except Exception as e:
        return f"Błąd komunikacji z API Confluence: {str(e)}"