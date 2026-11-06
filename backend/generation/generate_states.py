import json
from pathlib import Path
from fetching.fetch_rest_countries import fetch_rest_countries

DATA_PATH = (Path(__file__).resolve().parent.parent/ "data"/ "states.json")

def generate_states():
    countries = fetch_rest_countries()
    states = list(countries.values())
    for state in states:
        required_fields = [
            "name",
            "iso_code",
            "region",
            "subregion"
        ]

        for field in required_fields:
            if not state.get(field):
                raise ValueError(
                    f"Missing {field} in country record: {state}"
                )

    # Ensure the dataset is sufficiently complete.
    if len(states) < 200:
        raise ValueError(
            f"Unexpectedly few states: {len(states)}"
        )

    # Sort countries alphabetically.
    states.sort(key=lambda state: state["name"])

    # Create the data directory if necessary.
    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)

    # Write the validated dataset.
    with open(DATA_PATH, "w", encoding="utf-8") as file:
        json.dump(states, file, indent=4, ensure_ascii=False)

    print(f"Generated {len(states)} states in {DATA_PATH}")

if __name__ == "__main__":
    generate_states()
