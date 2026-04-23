
---

## main.py

```python
import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"


def scrape_website():
    try:
        response = requests.get(url)
        response.raise_for_status()
    except Exception as error:
        print(f"Failed to fetch website: {error}")
        return

    soup = BeautifulSoup(response.text, "html.parser")

    titles = soup.find_all("span", class_="titleline")

    print("Top News:")
    print("---------")

    for index, title in enumerate(titles[:10], start=1):
        link = title.find("a")
        print(f"{index}. {link.text}")
        print(link["href"])
        print()


if __name__ == "__main__":
    scrape_website()
