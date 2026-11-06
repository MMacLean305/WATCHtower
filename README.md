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

## Current Development Progress

The project is currently in its early development stage, with initial work focused on backend infrastructure and data management.

### Backend

- Flask application with SQLAlchemy database integration.
- Database models defined for states, risk assessments, risk history, geopolitical events, and data sources.
- Country and regional data retrieval from the UN M49 classification table.
- State data seeding utility for database initialization.
- Reusable HTTP client supporting retry and exponential backoff.
- JSON storage for country metadata and geopolitical overviews.

### Not Yet Implemented

- REST API endpoints.
- Automated geopolitical event ingestion.
- Risk-scoring calculations.
- Historical risk analysis.
- Interactive frontend and world map.
- Travel advisory integration.

The existing data retrieval and seeding utilities provide the foundation for future ingestion pipelines but do not yet constitute a complete automated data processing system.

## Technology Stack

**Current Backend**
- Python
- Flask
- Flask-SQLAlchemy
- SQLite
- Requests
- Beautiful Soup

**Planned Components**
- Interactive frontend and geographic visualization
- REST API
- Automated data ingestion pipelines
- Risk assessment and historical analysis components

Additional technologies will be selected as development progresses.

## Installation and Setup

### Requirements

- Python 3.9 or later
- pip

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
.venv\Scripts\Activate.ps1
```

**macOS / Linux**

```bash
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
python -m pip install Flask Flask-SQLAlchemy python-dotenv requests beautifulsoup4
```

### 4. Run the Backend

From the `backend` directory:

```bash
cd backend
flask --app app run --debug
```

The application uses a local SQLite database by default.

Set the `DATABASE_URL` environment variable to configure an alternative SQLAlchemy-compatible database connection.

## Data Initialization

### Fetch Country Data

To retrieve country and regional information from the UN M49 table, run the following from the `backend` directory:

```bash
python -m seeding.fetch_states
```

The retrieved information is stored in:

```text
backend/data/states.json
```

This operation requires an internet connection.

A separate state seeding utility is located at `backend/seeding/seed_states.py`. Database seeding and initialization workflows are still being developed.

## Project Structure

```text
WATCHtower/
├── README.md
├── docs/
│   └── WATCHtower_Project_Proposal.pdf
├── backend/
│   ├── app.py
│   ├── database.py
│   ├── data/
│   │   ├── states.json
│   │   └── state-overviews.json
│   ├── ingestion/
│   │   └── http_client.py
│   ├── models/
│   │   ├── state.py
│   │   ├── source.py
│   │   ├── event.py
│   │   ├── risk.py
│   │   └── risk_history.py
│   └── seeding/
│       ├── fetch_states.py
│       └── seed_states.py
```

The structure above reflects the current backend organization and the proposed documentation location.

## Project Documentation

For a more detailed explanation of WATCHtower's objectives, intended functionality, and development scope, see the:

[WATCHtower Project Overview and Objectives](docs/WATCHtower_Project_Proposal.pdf)

## Development Roadmap

- [x] Establish initial Flask backend architecture
- [x] Define core database models
- [x] Implement initial UN M49 country data retrieval
- [ ] Complete and validate country database seeding
- [ ] Implement REST API endpoints
- [ ] Integrate initial geopolitical event data sources
- [ ] Develop interactive world map and country profiles
- [ ] Integrate U.S. Department of State travel advisories
- [ ] Implement initial geopolitical risk indicators
- [ ] Develop composite risk-scoring methodology
- [ ] Implement historical risk visualization
- [ ] Test and deploy initial release

## Author

**Matthew MacLean**

University of Florida — Computer Science