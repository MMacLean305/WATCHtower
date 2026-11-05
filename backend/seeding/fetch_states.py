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


def fetch_states():
    response = requests.get(URL, timeout=30)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    # Locate the English-language M49 table
    table = None

    for candidate in soup.find_all("table"):
        headers = [
            th.get_text(" ", strip=True)
            for th in candidate.find_all("th")
        ]

        if (
            "Country or Area" in headers
            and "ISO-alpha3 Code" in headers
            and "Region Name" in headers
        ):
            table = candidate
            break

    if table is None:
        raise ValueError("Could not find the UN M49 English table")

    headers = [
        th.get_text(" ", strip=True)
        for th in table.find_all("th")
    ]

    states = []
    seen_codes = set()

    for row in table.find_all("tr"):
        cells = row.find_all("td")

        if len(cells) != len(headers):
            continue

        values = [
            cell.get_text(" ", strip=True)
            for cell in cells
        ]

        record = dict(zip(headers, values))

        iso_code = record["ISO-alpha3 Code"]

        if not iso_code or iso_code in seen_codes:
            continue

        seen_codes.add(iso_code)

        states.append({
            "name": record["Country or Area"],
            "official_name": None,
            "iso_code": iso_code,
            "region": record["Region Name"] or "Unclassified",
            "subregion": record["Sub-region Name"] or None
        })

    if len(states) < 200:
        raise ValueError(
            f"Unexpectedly few records: {len(states)}"
        )

    states.sort(key=lambda state: state["name"])

    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)

    with open(DATA_PATH, "w", encoding="utf-8") as file:
        json.dump(states, file, indent=4, ensure_ascii=False)

    print(f"Saved {len(states)} records to {DATA_PATH}")


if __name__ == "__main__":
    fetch_states()
