
import os
import requests
from dotenv import load_dotenv

load_dotenv()
REST_COUNTRIES_URL = "https://api.restcountries.com/countries/v5"

def fetch_rest_countries():
    api_key = os.getenv("REST_COUNTRIES_API_KEY")
    if not api_key:
        raise ValueError("REST_COUNTRIES_API_KEY is not configured")
    headers = {"Authorization": f"Bearer {api_key}"}

    countries = {}
    limit = 100
    offset = 0

    while True:
        params = {"limit": limit,"offset": offset,"response_fields": ("names.common,names.official,codes.alpha_3,""region,subregion,latlng")}
        response = requests.get(REST_COUNTRIES_URL,headers=headers,params=params,timeout=30)

        response.raise_for_status()

        data = response.json()["data"]
        records = data["objects"]

        for record in records:
            codes = record.get("codes") or {}
            names = record.get("names") or {}
            iso_code = codes.get("alpha_3")
            name = names.get("common")
            official_name = names.get("official")

            # Skip incomplete country records.
            if not iso_code or not name:
                continue

            # Prevent duplicate ISO3 codes.
            if iso_code in countries:
                raise ValueError(f"Duplicate ISO3 code: {iso_code}")

            countries[iso_code] = {"name": name, "official_name": official_name, "iso_code": iso_code, "region": record.get("region") or "Unclassified","subregion": record.get("subregion") or "Unclassified","latlng": record.get("latlng")}
        if not data["meta"]["more"]:
            break
        offset += limit

    # Validate the complete dataset.
    if len(countries) < 200:
        raise ValueError(
            f"Unexpectedly few records: {len(countries)}"
        )
    return countries

if __name__ == "__main__":
    countries = fetch_rest_countries()

    print(f"Fetched {len(countries)} countries")

    for iso_code in ["FRA", "UGA", "GBR"]:
        print(f"{iso_code}: {countries.get(iso_code)}")
