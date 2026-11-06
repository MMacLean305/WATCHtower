# WATCHtower

**Worldwide Analysis of Threats, Conflicts & Hazards**

WATCHtower is an early-stage geopolitical intelligence and visualization platform designed to aggregate, organize, and present information concerning international developments and state-level conditions.

The platform aims to consolidate geopolitical information from established governmental, international, and research-based sources into a centralized application. Through interactive geographic visualizations, country profiles, historical event records, and risk indicators, WATCHtower seeks to make geopolitical information more accessible and easier to interpret.

**The primary objective of WATCHtower is to help users understand current geopolitical conditions, monitor significant international developments, and examine how conditions evolve over time.**

## Planned Features

- **Interactive World Map:** Explore countries and visualize geopolitical events through a geographic interface.
- **Country Profiles:** Access country-specific information, geopolitical developments, travel advisories, and relevant news.
- **Geopolitical Event Monitoring:** Aggregate and organize international events from supported external data sources.
- **Risk Assessment:** Evaluate country-level conditions using six geopolitical risk factors and a composite risk score.
- **Historical Analysis:** Track changes in geopolitical risk through historical records and graphical visualizations.
- **Data Transparency:** Identify the original sources and update dates associated with geopolitical information.

These features represent the intended functionality of WATCHtower and will be implemented incrementally.

## Geopolitical Risk Assessment

WATCHtower aims to develop a quantitative risk assessment framework that evaluates six major dimensions of geopolitical risk.

| Risk Factor | Description |
|---|---|
| Political | Government stability, corruption, and institutional effectiveness |
| Economic | Inflation, sovereign debt, unemployment, and economic vulnerability |
| Conflict | Armed conflict, casualties, and military activity |
| Terrorism | Terrorist incidents, fatalities, and threats |
| Crime | Violent crime, organized crime, and homicide rates |
| Civil Unrest | Riots, demonstrations, and political violence |

Each risk factor is intended to contribute to a composite country-level risk score ranging from **0 to 100**.

The purpose of this score is to provide users with a general understanding of current geopolitical conditions, rather than predict future conflicts or political developments.

The scoring methodology is currently under development. Individual risk indicators, weighting methods, and historical calculations have not yet been implemented.

## Proposed Data Sources

WATCHtower intends to integrate data from established sources, potentially including:

- **United Nations (UN):** Country and regional classifications.
- **International Monetary Fund (IMF):** Economic and financial indicators.
- **World Bank:** Economic development and governance indicators.
- **UCDP:** Armed conflict and conflict-related fatalities.
- **ACLED:** Political violence, demonstrations, and conflict events.
- **U.S. Department of State:** Country-specific travel advisories.

Data source integration will occur incrementally, subject to availability, access requirements, and technical compatibility.

### Currently Integrated Data Source

**United Nations M49 Geographic Classification**

WATCHtower currently retrieves country and area information from the United Nations M49 geographic classification system.

The retrieved dataset contains **248 country and area records**, including standardized geographic identifiers, country or area names, and regional classifications.

The data is stored locally in JSON format and can be imported into the PostgreSQL database using the project's seeding utilities.

Official source: https://unstats.un.org/unsd/methodology/m49/

## Current Development Progress

The project is currently in its early development stage, with initial work focused on backend infrastructure, database architecture, and data management.

### Backend

- Flask application with SQLAlchemy database integration.
- PostgreSQL configured as the primary relational database.
- Database models defined for states, risk assessments, risk history, geopolitical events, and data sources.
- Database schema successfully initialized in PostgreSQL.
- Country and regional data retrieval from the UN M49 classification table.
- JSON-based storage of retrieved country and area metadata.
- State data seeding utility successfully tested with **248 records inserted into PostgreSQL**.
- Environment-based database configuration using `DATABASE_URL`.
- Reusable HTTP client supporting retry and exponential backoff.
- Initial infrastructure for future geopolitical data ingestion and processing.

### Database Architecture

WATCHtower uses **PostgreSQL** for persistent relational data storage and **SQLAlchemy** for object-relational mapping.

The current database contains five primary tables:

| Table | Purpose |
|---|---|
| `states` | Country and area identification and geographic information |
| `sources` | Information source metadata and attribution |
| `events` | Geopolitical events associated with countries and sources |
| `risks` | Country-level geopolitical risk assessments |
| `risk_history` | Historical records of geopolitical risk assessments |

The `states` table has been successfully populated with 248 records. The remaining tables are initialized and will be populated as their associated functionality is developed.

The database architecture is intended to support structured geopolitical analysis, source traceability, and historical comparisons.

### Not Yet Implemented

- REST API endpoints.
- Automated geopolitical event ingestion.
- Risk-scoring calculations.
- Historical risk analysis.
- Interactive frontend and world map.
- Travel advisory integration.
- Production deployment.

The existing data retrieval and seeding utilities provide the foundation for future ingestion pipelines but do not yet constitute a complete automated geopolitical data processing system.

## Technology Stack

**Current Backend**
- Python
- Flask
- Flask-SQLAlchemy
- PostgreSQL
- Psycopg
- Flask-Migrate (installed for database migration tooling)
- Requests
- Beautiful Soup
- python-dotenv

**Development Tools**
- Git and GitHub
- PyCharm
- pgAdmin 4
- Python virtual environments

**Planned Components**
- Interactive frontend and geographic visualization
- REST API
- Automated data ingestion pipelines
- Risk assessment and historical analysis components
- Country-specific dashboards and event timelines

Additional technologies will be selected as development progresses.

## Installation and Setup

### Requirements

- Python 3.9 or later, with a version compatible with the installed dependencies
- pip
- PostgreSQL
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/MMacLean305/WATCHtower.git
cd WATCHtower
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the environment:

**Windows (PowerShell)**

```powershell
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux**

```bash
source .venv/bin/activate
```

### 3. Install Dependencies

Install the required Python packages using the project's dependency file:

```bash
python -m pip install -r requirements.txt
```

### 4. Configure PostgreSQL

WATCHtower uses PostgreSQL as its primary database.

Create a PostgreSQL database named:

```text
watchtower
```

This can be done through pgAdmin or PostgreSQL's command-line tools.

Inside the `backend` directory, create a `.env` file containing:

```dotenv
DATABASE_URL=postgresql+psycopg://postgres:YOUR_PASSWORD@localhost:5432/watchtower
```

Replace `YOUR_PASSWORD` with your local PostgreSQL password.

The database username, host, and port should be adjusted if your PostgreSQL configuration differs.

**Security:** The `.env` file is excluded from Git tracking through `.gitignore`. Never commit database credentials or other sensitive information to the repository.

### 5. Run the Backend

Navigate to the `backend` directory:

```bash
cd backend
```

Start the Flask development server:

```bash
flask --app app run --debug
```

The Flask application uses the configured `DATABASE_URL` to connect to PostgreSQL.

The current backend initializes its database tables through SQLAlchemy's `db.create_all()` functionality.

Although Flask-Migrate is included in the project's dependencies, a complete version-controlled database migration workflow has not yet been established.

## Data Initialization

### Fetch Country Data

To retrieve country and regional information from the UN M49 classification table, run the following from the `backend` directory:

```bash
python -m seeding.fetch_states
```

The retrieved information is stored in:

```text
backend/data/states.json
```

This operation requires an internet connection.

The current dataset contains 248 country and area records.

### Seed the PostgreSQL Database

After configuring PostgreSQL and initializing the database schema, run:

```bash
python -m seeding.seed_states
```

This utility reads the local `states.json` dataset and inserts state records into PostgreSQL.

The seeding process has been successfully tested, producing:

```text
Added 248 states. Skipped 0 existing states.
```

The utility checks for existing records to avoid inserting duplicates during repeated execution.

### Verify Database Initialization

To verify the country records, run the following from the `backend` directory:

```powershell
python -c "from app import app; from models import State; ctx = app.app_context(); ctx.push(); print('Total states:', State.query.count()); ctx.pop()"
```

A successfully populated database should return:

```text
Total states: 248
```

The current database schema also includes the `events`, `sources`, `risks`, and `risk_history` tables, which will be populated during later development phases.

## Project Structure

```text
WATCHtower/
├── README.md
├── .gitignore
├── requirements.txt
├── DOCS/
│   └── WATCHtower Project Overview and Objectives.pdf
├── backend/
│   ├── app.py
│   ├── database.py
│   ├── .env                  # Local configuration (not tracked)
│   ├── data/
│   │   ├── states.json
│   │   └── state-overviews.json
│   ├── ingestion/
│   │   └── http_client.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── state.py
│   │   ├── source.py
│   │   ├── event.py
│   │   ├── risk.py
│   │   └── risk_history.py
│   └── seeding/
│       ├── __init__.py
│       ├── fetch_states.py
│       └── seed_states.py
└── frontend/
```

The structure above reflects the current backend organization and is expected to expand as API routes, ingestion pipelines, tests, and frontend components are implemented.

## Project Documentation

For a more detailed explanation of WATCHtower's objectives, intended functionality, and development scope, see:

[WATCHtower Project Overview and Objectives](DOCS/WATCHtower%20Project%20Overview%20and%20Objectives.pdf)

## Development Roadmap

### Phase 1 — Backend Foundation
- [x] Establish initial Flask backend architecture
- [x] Define core database models
- [x] Implement initial UN M49 country data retrieval
- [x] Establish reusable HTTP request infrastructure

### Phase 2 — Database Infrastructure
- [x] Configure PostgreSQL database
- [x] Integrate PostgreSQL with Flask-SQLAlchemy
- [x] Initialize relational database tables
- [x] Complete and validate country database seeding
- [x] Populate database with 248 country and area records
- [ ] Establish version-controlled database schema migrations

### Phase 3 — API and Data Ingestion
- [ ] Implement REST API endpoints
- [ ] Develop country information retrieval endpoints
- [ ] Integrate initial geopolitical event data sources
- [ ] Implement automated geopolitical event ingestion
- [ ] Integrate U.S. Department of State travel advisories

### Phase 4 — Risk Assessment
- [ ] Implement initial geopolitical risk indicators
- [ ] Develop composite risk-scoring methodology
- [ ] Implement risk history storage and retrieval
- [ ] Develop historical risk visualization

### Phase 5 — Frontend and Deployment
- [ ] Develop interactive world map and country profiles
- [ ] Integrate backend API with frontend
- [ ] Implement geopolitical event and risk dashboards
- [ ] Test and deploy initial release

## Author

**Matthew MacLean**

University of Florida — Computer Science

GitHub: https://github.com/MMacLean305