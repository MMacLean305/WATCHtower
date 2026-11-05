# WATCHtower

WATCHtower (Worldwide Analysis of Threats, Conflicts & Hazards) is an early-stage geopolitical intelligence platform for organizing country data, events, and risk assessments.

## Current progress

- A Flask backend initializes a SQLAlchemy database and creates its tables at startup.
- Database models are defined for states, risk assessments, risk history, events, and data sources.
- A script can fetch country and region data from the UN M49 table into `backend/data/states.json`.
- A state seeding script and a reusable HTTP session with retry/backoff behavior are present.
- State overview data is stored in `backend/data/state-overviews.json`.

The project does not yet include API routes, event-source ingestion, or risk-scoring logic. The seeding and ingestion components are foundations, not a complete automated data pipeline.

## Requirements

- Python 3.9 or later
- pip

## Setup

From the repository root, create and activate a virtual environment and install the backend dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install Flask Flask-SQLAlchemy python-dotenv requests beautifulsoup4
```

## Run the backend

Start the Flask development server from the `backend` directory:

```bash
cd backend
flask --app app run --debug
```

The app uses a local SQLite database by default. Set `DATABASE_URL` to use another SQLAlchemy-compatible database URL.

## Fetch state data

To refresh `backend/data/states.json` from the UN M49 table, run this from the `backend` directory:

```bash
python -m seeding.fetch_states
```

This command requires an internet connection. The state seeding utility is also in `backend/seeding/`; database initialization and seeding are still being developed.

## Project layout

```text
backend/
  app.py                    # Flask application setup
  database.py               # SQLAlchemy extension
  data/
    states.json             # State data used by the seeding workflow
    state-overviews.json    # State overview data
  ingestion/
    http_client.py          # Requests session with GET retry/backoff
  models/                   # State, risk, event, source, and history models
  seeding/
    fetch_states.py         # Fetch state data from UN M49
    seed_states.py          # Seed states into the database
```

## Author

Matthew MacLean
