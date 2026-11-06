
import os
import requests
from dotenv import load_dotenv

load_dotenv()
NEWSAPI_URL = "https://newsapi.org/v2/everything"

def fetch_newsapi_news(query, page_size=20):
    api_key = os.getenv("NEWSAPI_KEY")

    if not api_key:
        raise ValueError("NEWSAPI_KEY is not configured")

    params = {"q": query, "pageSize": page_size, "sortBy": "publishedAt", "apiKey": api_key}

    response = requests.get(NEWSAPI_URL, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()
    return data["articles"]

