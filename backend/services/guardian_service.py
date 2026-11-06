import os
import requests
from dotenv import load_dotenv
load_dotenv()

GUARDIAN_URL = "https://content.guardianapis.com/search"

def fetch_guardian_news(page_size=50):
    api_key = os.getenv("GUARDIAN_API_KEY")
    if not api_key:
        raise ValueError("GUARDIAN_API_KEY is not configured")
    params = {"api-key": api_key, "section": "world", "page-size": page_size, "order-by": "newest", "show-fields": "trailText,thumbnail"}

    response = requests.get(GUARDIAN_URL, params=params, timeout=10)
    response.raise_for_status()
    return response.json()["response"]["results"]