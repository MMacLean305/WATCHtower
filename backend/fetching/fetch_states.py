import json
from pathlib import Path
import requests
from bs4 import BeautifulSoup
URL = "https://unstats.un.org/unsd/methodology/m49/overview/"

DATA_PATH = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "states.json"
)

REQUIRED_HEADERS = {
    "Country or Area",
    "ISO-alpha3 Code",
    "Region Name",
    "Sub-region Name",
}


def fetch_states():
    response = requests.get(URL, timeout=30)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    table = None
    headers = None

    # Locate the English-language UN M49 table.
    for candidate in soup.find_all("table"):
        first_row = candidate.find("tr")

        if first_row is None:
            continue

        candidate_headers = [
            cell.get_text(" ", strip=True)
            for cell in first_row.find_all(["th", "td"])
        ]

        if REQUIRED_HEADERS.issubset(set(candidate_headers)):
            table = candidate
            headers = candidate_headers
            break

    if table is None:
        raise ValueError("Could not find the UN M49 English table")

    states = []
    seen_codes = set()

    # Skip the first row because it contains column headers.
    for row in table.find_all("tr")[1:]:
        cells = row.find_all(["td", "th"])

        if len(cells) != len(headers):
            continue

        values = [
            cell.get_text(" ", strip=True)
            for cell in cells
        ]

        record = dict(zip(headers, values))

        iso_code = record["ISO-alpha3 Code"].strip()
        name = record["Country or Area"].strip()

        if not iso_code or not name:
            continue

        if iso_code in seen_codes:
            continue

        seen_codes.add(iso_code)

        states.append({
            "name": name,
            "official_name": None,
            "iso_code": iso_code,
            "region": record["Region Name"] or "Unclassified",
            "subregion": record["Sub-region Name"] or None
        })

    # Validate the dataset before overwriting existing data.
    if len(states) < 200:
        raise ValueError(
            f"Unexpectedly few records: {len(states)}"
        )

    states.sort(key=lambda state: state["name"])

    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)

    with open(DATA_PATH, "w", encoding="utf-8") as file:
        json.dump(
            states,
            file,
            indent=4,
            ensure_ascii=False
        )

    print(f"Saved {len(states)} records to {DATA_PATH}")


if __name__ == "__main__":
    fetch_states()
