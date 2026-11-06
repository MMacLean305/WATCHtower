# WATCHtower

**Worldwide Analysis of Threats, Conflicts & Hazards**

WATCHtower is an early-stage geopolitical intelligence and visualization platform designed to aggregate, organize, and present information concerning international developments and state-level conditions.

The platform aims to consolidate geopolitical information from governmental agencies, international organizations, academic institutions, research organizations, and other established data providers into a centralized application. Through interactive geographic visualizations, country profiles, historical event records, and risk indicators, WATCHtower seeks to make geopolitical information more accessible and easier to interpret.

**The primary objective of WATCHtower is to help users understand current geopolitical conditions, monitor significant international developments, and examine how conditions evolve over time.**

The project is currently focused on backend infrastructure, database development, and establishing the foundations for future geopolitical data ingestion and analysis.

## Planned Features

- **Interactive World Map:** Explore countries and visualize geopolitical events through a geographic interface.
- **Country Profiles:** Access country-specific information, geopolitical developments, travel advisories, and relevant news.
- **Geopolitical Event Monitoring:** Aggregate and organize international events from a variety of external data sources.
- **Risk Assessment:** Evaluate country-level conditions using six geopolitical risk factors and a composite risk score.
- **Historical Analysis:** Track changes in geopolitical conditions and risk assessments through historical records and graphical visualizations.
- **Data Transparency:** Identify the original sources, publication dates, and update information associated with geopolitical data.
- **Country Comparisons:** Compare geopolitical conditions and risk indicators across different countries and regions.

These features represent the intended functionality of WATCHtower and will be implemented incrementally as the platform develops.

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

The scoring methodology is currently under development. Individual risk indicators, data normalization techniques, weighting methods, and historical calculations have not yet been implemented.

Future development will focus on creating a transparent, reproducible methodology that incorporates measurable indicators from reliable data sources.

## Data Sources

WATCHtower is designed to aggregate geopolitical information from a broad range of authoritative and publicly accessible sources.

The platform's long-term objective is to incorporate data from numerous governmental, international, academic, and research-based organizations, rather than rely on a limited number of providers.

Potential sources include, but are not limited to:

| Category | Potential Sources |
|---|---|
| Geographic and Demographic | United Nations, World Bank, national statistical agencies |
| Economic and Financial | International Monetary Fund, World Bank, OECD, central banks |
| Armed Conflict | UCDP, ACLED, conflict research institutions |
| Terrorism and Security | Global Terrorism Database, government security reports |
| Political Stability and Governance | World Bank Governance Indicators, V-Dem, Freedom House |
| Crime and Public Safety | UNODC, national crime statistics |
| Civil Unrest | ACLED, governmental and academic datasets |
| Travel Advisories | U.S. Department of State, UK FCDO, other national foreign ministries |
| Current Events | International news organizations, official government publications, verified reporting |

These sources represent potential integration opportunities, not a finalized or exhaustive list.

Additional providers will be evaluated as development progresses. Source selection will consider reliability, geographic coverage, update frequency, licensing requirements, accessibility, and technical compatibility.

### Currently Integrated Data

**United Nations M49 Geographic Classification**

WATCHtower currently supports retrieving geographic classification data from the United Nations M49 system.

The initial dataset contains **248 country and area records**, including standardized geographic identifiers, country or area names, and regional classifications.

These records are stored locally in JSON format and have been successfully imported into the PostgreSQL database.

Official source: https://unstats.un.org/unsd/methodology/m49/

Additional geopolitical data integrations remain under development.

## Current Development Progress

WATCHtower is currently in the early stages of development, with initial work concentrated on backend architecture, relational database infrastructure, and geographic data retrieval.

### Implemented Backend Components

- Initial Flask application and backend structure.
- SQLAlchemy integration for relational data management.
- PostgreSQL database configuration and connectivity.
- Database models for states, sources, geopolitical events, risk assessments, and risk history.
- Initial relational database table creation.
- Environment-based database configuration.
- UN M49 geographic data retrieval utility.
- JSON storage for retrieved country and area records.
- Database seeding utility tested with 248 records.
- Reusable HTTP client supporting retry and exponential backoff.

### Current Limitations

The existing backend provides an initial technical foundation but does not yet implement the platform's primary geopolitical monitoring and analytical capabilities.

The following components remain under development:

- REST API endpoints.
- Automated geopolitical event ingestion.
- External source management and event normalization.
- Risk assessment calculations.
- Composite geopolitical risk scoring.
- Historical risk analysis.
- Interactive geographic visualization.
- Country dashboards and profiles.
- Travel advisory integration.
- Automated backend testing and production deployment.

The current geographic data pipeline is an initial proof of concept for retrieving and storing structured external information. It does not yet represent a complete geopolitical data collection system.

## Database Architecture

WATCHtower uses **PostgreSQL** as its primary relational database, with **Flask-SQLAlchemy** providing object-relational mapping.

The current backend defines five primary database tables:

| Table | Purpose |
|---|---|
| `states` | Stores country and area identifiers and geographic information |
| `sources` | Stores information source metadata and attribution |
| `events` | Represents geopolitical events and developments |
| `risks` | Represents country-level geopolitical risk assessments |
| `risk_history` | Supports historical risk tracking and analysis |

The initial database schema has been created successfully.

The `states` table has been populated with 248 records retrieved from the United Nations M49 classification system. The remaining tables are currently empty and will be populated as their associated features are implemented.

### Database Management

Database connectivity is configured through the `DATABASE_URL` environment variable.

The application currently initializes its database tables using SQLAlchemy's `db.create_all()` functionality.

Flask-Migrate has been installed as a dependency, but a version-controlled database migration workflow has not yet been established.

As the database schema evolves, migration tooling will be incorporated to manage structural changes without relying exclusively on automatic table creation.

## Technology Stack

### Current Backend

- **Python:** Primary backend programming language.
- **Flask:** Web application framework.
- **Flask-SQLAlchemy:** Object-relational mapping and database integration.
- **PostgreSQL:** Relational database management system.
- **Psycopg:** PostgreSQL database driver.
- **Requests:** HTTP communication with external data sources.
- **Beautiful Soup:** Parsing and extracting structured information from external web resources.
- **python-dotenv:** Environment-based application configuration.
- **Flask-Migrate:** Installed for future database migration management.

### Development Tools

- Git and GitHub
- PyCharm
- pgAdmin 4
- Python virtual environments

### Planned Components

- RESTful API architecture.
- Automated geopolitical data ingestion pipelines.
- Interactive frontend and geographic visualization.
- Country information dashboards.
- Geopolitical risk assessment and historical analysis.
- Data visualization and comparative analytics.
- Testing, monitoring, and deployment infrastructure.

Additional technologies will be selected as the platform's requirements evolve.

## Installation and Setup

### Requirements

- Python 3.9 or later, with a version compatible with the installed dependencies.
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

Install the project's Python dependencies:

```bash
python -m pip install -r requirements.txt
```

### 4. Configure PostgreSQL

WATCHtower uses PostgreSQL as its primary database.

Create a local PostgreSQL database named:

```text
watchtower
```

This can be accomplished through pgAdmin or PostgreSQL's command-line utilities.

Inside the `backend` directory, create a `.env` file with the following configuration:

```dotenv
DATABASE_URL=postgresql+psycopg://postgres:YOUR_PASSWORD@localhost:5432/watchtower
```

Replace `YOUR_PASSWORD` with the password associated with your local PostgreSQL installation.

Adjust the username, hostname, and port if your PostgreSQL configuration differs.

**Security:** Environment files containing database credentials are excluded from version control through `.gitignore`. Never commit passwords, API keys, or other sensitive credentials.

### 5. Run the Backend

Navigate to the backend directory:

```bash
cd backend
```

Start the Flask development server:

```bash
flask --app app run --debug
```

The application uses the configured PostgreSQL connection and currently initializes its database schema through SQLAlchemy.

The Flask development server is intended for local development and testing.

## Data Initialization

### Fetch Country Data

From the `backend` directory, retrieve country and area information from the United Nations M49 classification table:

```bash
python -m seeding.fetch_states
```

The retrieved information is saved to:

```text
backend/data/states.json
```

This operation requires an internet connection.

The initial dataset contains 248 country and area records.

### Seed the PostgreSQL Database

After configuring the database and initializing the application, run:

```bash
python -m seeding.seed_states
```

The seeding utility reads the local JSON dataset and inserts records into PostgreSQL.

The initial seeding process was successfully tested with the following result:

```text
Added 248 states. Skipped 0 existing states.
```

The utility checks for existing records to avoid inserting duplicates during repeated execution.

### Verify Database Records

To verify that the country records were imported successfully, run the following from the `backend` directory:

```powershell
python -c "from app import app; from models import State; ctx = app.app_context(); ctx.push(); print('Total states:', State.query.count()); ctx.pop()"
```

A successfully populated database should return:

```text
Total states: 248
```

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
│   ├── .env
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

The structure above reflects the current backend organization and will expand as additional components are implemented.

The `.env` file is used for local configuration and is not tracked in the repository.

## Project Documentation

For a more detailed explanation of WATCHtower's objectives, intended functionality, and development scope, see:

[WATCHtower Project Overview and Objectives](DOCS/WATCHtower%20Project%20Overview%20and%20Objectives.pdf)

## Development Roadmap

WATCHtower is currently focused on establishing its backend foundation and developing the initial data infrastructure required for future geopolitical analysis.

The roadmap below tracks individual milestones rather than treating entire development phases as complete.

### Phase 1 — Backend Architecture and Infrastructure

- [x] Establish initial Flask application.
- [x] Define core SQLAlchemy database models.
- [x] Configure PostgreSQL database connection.
- [x] Initialize initial relational database tables.
- [x] Configure environment-based database credentials.
- [ ] Establish version-controlled database schema migrations.
- [ ] Implement comprehensive input validation and error handling.
- [ ] Develop automated backend tests.

### Phase 2 — Geographic Data and Country Information

- [x] Implement initial UN M49 data retrieval.
- [x] Store retrieved country and area information in JSON.
- [x] Implement and test initial PostgreSQL state seeding.
- [ ] Validate and refine country metadata.
- [ ] Develop country information REST API endpoints.
- [ ] Expand country profiles with additional geographic, demographic, and political information.
- [ ] Establish periodic country data updates.

### Phase 3 — Geopolitical Data Collection

- [ ] Evaluate and select external geopolitical data providers.
- [ ] Implement source registration and metadata management.
- [ ] Develop initial geopolitical event ingestion pipeline.
- [ ] Normalize and validate incoming geopolitical event data.
- [ ] Associate geopolitical events with relevant countries and sources.
- [ ] Implement recurring data retrieval and update workflows.
- [ ] Expand coverage across geopolitical data categories.

### Phase 4 — Risk Assessment and Historical Analysis

- [ ] Define measurable indicators for the six geopolitical risk dimensions.
- [ ] Establish data normalization and weighting methodologies.
- [ ] Implement individual risk-factor calculations.
- [ ] Develop composite country-level risk scoring.
- [ ] Store and retrieve historical risk assessments.
- [ ] Implement historical trends and comparative analysis.
- [ ] Validate and document the risk assessment methodology.

### Phase 5 — Frontend and Visualization

- [ ] Select frontend technologies and mapping framework.
- [ ] Develop interactive world map.
- [ ] Implement country profiles and information dashboards.
- [ ] Display geopolitical events geographically.
- [ ] Visualize individual and composite risk indicators.
- [ ] Develop historical charts and country comparisons.
- [ ] Integrate frontend with backend REST API.

### Phase 6 — Testing, Deployment, and Expansion

- [ ] Implement comprehensive integration and API testing.
- [ ] Improve data collection reliability and monitoring.
- [ ] Optimize database queries and backend performance.
- [ ] Implement production deployment infrastructure.
- [ ] Conduct usability and performance testing.
- [ ] Deploy initial public release.
- [ ] Expand geographic coverage, data sources, and analytical capabilities.

## Disclaimer

WATCHtower is an independent software development project intended for educational, informational, and analytical purposes.

Any future geopolitical risk indicators will represent descriptive assessments based on available data and should not be interpreted as predictions of future events, official intelligence assessments, or professional security recommendations.

## Author

**Matthew MacLean**

University of Florida — Computer Science

GitHub: https://github.com/MMacLean305