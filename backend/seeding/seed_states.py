import json
from pathlib import Path
from app import app
from database import db
from models import State

DATA_PATH = (Path(__file__).resolve().parent.parent/ "data"/ "states.json")

def seed_states():
    with open(DATA_PATH, "r", encoding="utf-8") as file:
        states = json.load(file)
    added = 0
    updated = 0
    with app.app_context():
        try:
            for state_data in states:
                iso_code = state_data["iso_code"]
                existing = State.query.filter_by(iso_code=iso_code).first()
                if existing:
                    existing.name = state_data["name"]
                    existing.official_name = state_data.get("official_name")
                    existing.region = state_data.get("region", "Unclassified")
                    existing.subregion = state_data.get("subregion", "Unclassified")
                    updated += 1
                else:
                    state = State(name=state_data["name"],official_name=state_data.get("official_name"),iso_code=iso_code,region=state_data.get("region", "Unclassified"),subregion=state_data.get("subregion", "Unclassified"))
                    db.session.add(state)
                    added += 1
            db.session.commit()
        except Exception:
            db.session.rollback()
            raise
    print(f"Added {added} states.")
    print(f"Updated {updated} existing states.")

if __name__ == "__main__":
    seed_states()
