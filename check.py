import requests, json, os, sys
from urllib.parse import urljoin
from bs4 import BeautifulSoup


URL = "https://egy.voxcinemas.com"
TOKEN = os.environ["TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]
FILE = "seen.json"


html = requests.get(URL, timeout=20, headers={"User-Agent":
"Mozilla/5.0"}).text
soup = BeautifulSoup(html, "html.parser")


movies = {}
for a in soup.select('a[href*="/movie-details/"]'):
    name = a.get("title") or a.get_text(strip=True)
    if name:
        movies[a["href"]] = name


print("لقيت", len(movies), "فيلم")
