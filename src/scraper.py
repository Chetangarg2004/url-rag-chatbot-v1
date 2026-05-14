import requests
from bs4 import BeautifulSoup

def scrape_urls(urls):
    all_text = ""

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    for url in urls:
        try:
            response = requests.get(url, headers=headers, timeout=10)
            soup = BeautifulSoup(response.text, "html.parser")

            text = soup.get_text()
            all_text += text

        except Exception as e:
            print(f"Error scraping {url}: {e}")

    return all_text