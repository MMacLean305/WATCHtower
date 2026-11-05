# WATCHtower

WATCHtower (Worldwide Analysis of Threats, Conflicts & Hazards) is a geopolitical intelligence platform that monitors global events, analyzes historical trends, and assesses geopolitical risk through data-driven analysis. This repository currently contains the initial Flask backend, including database models for state-level risks, events, and their data sources; API routes and data-loading workflows have not been added yet.

## Author
Matthew MacLean

## Requirements

- Python 3.9 or later
- pip

## Setup

From the repository root, create and activate a virtual environment, then install the backend dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install Flask Flask-SQLAlchemy python-dotenv
```

## Run

Start the Flask development server from the `backend` directory:

```bash
cd backend
flask --app app run --debug
```

The app uses a local SQLite database by default. Set `DATABASE_URL` to use a different SQLAlchemy-compatible database URL.

## Data models

- `State` stores state names, codes, regions, and overviews.
- `Risk` stores risk factor scores and an overall score for a state.
- `RiskHistory` stores dated risk scores.
- `Event` stores dated, geographically located events associated with a state and source.
- `Source` stores information about event data providers.

The database tables are created when the Flask app starts.

## Project layout

```text
backend/
	app.py                 # Flask application setup
	database.py            # SQLAlchemy extension
	data/states.json       # State data file
	models/                # Database models
```
