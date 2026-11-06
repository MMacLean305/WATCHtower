# WATCHtower

**Worldwide Analysis of Threats, Conflicts & Hazards**

WATCHtower is an early-stage geopolitical intelligence and visualization platform designed to aggregate, organize, and present information concerning international developments and state-level conditions.

The platform aims to consolidate geopolitical information from governmental agencies, international organizations, academic institutions, research organizations, and other established data providers into a centralized application. Through interactive geographic visualizations, country profiles, historical event records, and risk indicators, WATCHtower seeks to make geopolitical information more accessible and easier to interpret.

**The primary objective of WATCHtower is to help users understand current geopolitical conditions, monitor significant international developments, and examine how conditions evolve over time.**

The project is currently focused on backend infrastructure, REST API development, database management, and establishing the foundations for future geopolitical data ingestion and analysis.

## Planned Features

- **Interactive World Map:** Explore countries and visualize geopolitical events through a geographic interface.
- **Country Profiles:** Access country-specific information, geopolitical developments, travel advisories, and relevant news.
- **Geopolitical Event Monitoring:** Aggregate and organize international events from a variety of external data sources.
- **Risk Assessment:** Evaluate country-level conditions using six geopolitical risk factors and a composite risk score.
- **Historical Analysis:** Track changes in geopolitical conditions and risk assessments through historical records and graphical visualizations.
- **Data Transparency:** Identify original sources, publication dates, and update information associated with geopolitical data.
- **Country Comparisons:** Compare geopolitical conditions and risk indicators across countries and regions.

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

The scoring methodology is currently under development. Individual risk indicators, data normalization techniques, weighting methods, and historical calculations have not yet been implemented.

## Data Sources

WATCHtower is designed to aggregate geopolitical information from a broad range of authoritative and publicly accessible sources.

Potential data providers include, but are not limited to:

| Category | Potential Sources |
|---|---|
| Geographic and Demographic | United Nations, World Bank, national statistical agencies |
| Economic and Financial | IMF, World Bank, OECD, central banks |
| Armed Conflict | UCDP, ACLED, conflict research institutions |
| Terrorism and Security | Global Terrorism Database, government security reports |
| Political Stability and Governance | World Bank Governance Indicators, V-Dem, Freedom House |
| Crime and Public Safety | UNODC, national crime statistics |
| Civil Unrest | ACLED, governmental and academic datasets |
| Travel Advisories | U.S. Department of State, UK FCDO, other national foreign ministries |
| Current Events | International news organizations, official government publications, verified reporting |

These are potential integration opportunities, not a finalized or exhaustive list. Source selection will consider reliability, geographic coverage, update frequency, licensing requirements, accessibility, and technical compatibility.

### Currently Integrated Data

**United Nations M49 Geographic Classification**

WATCHtower currently supports retrieving geographic classification data from the United Nations M49 system.

The initial dataset contains **248 country and area records**, including standardized geographic identifiers, country or area names, and regional classifications.

These records are stored locally in JSON format and have been successfully imported into PostgreSQL.

Official source: https://unstats.un.org/unsd/methodology/m49/

Additional geopolitical data integrations remain under development.

## Current Development Progress

WATCHtower is in early development, with initial work concentrated on backend architecture, relational database infrastructure, geographic data retrieval, and REST API implementation.

### Implemented Backend Components

- Initial Flask application and modular backend structure.
- SQLAlchemy integration with PostgreSQL.
- Database models for states, sources, geopolitical events, risk assessments, and risk history.
- Initial relational database table creation.
- Environment-based database configuration.
- UN M49 geographic data retrieval utility.
- JSON storage for country and area records.
- Database seeding utility successfully tested with 248 records.
- Reusable HTTP client supporting retry and exponential backoff.
- Flask Blueprints for organizing state and event API endpoints.
- Reusable serialization functions for converting database models into JSON responses.
- Initial REST API endpoints for retrieving countries and geopolitical events.

### Current Limitations

Although the initial API endpoints have been implemented, the backend does not yet provide a complete geopolitical monitoring service.

Outstanding components include:

- Automated testing and comprehensive API validation.
- Pagination and advanced event filtering.
- Automated geopolitical event ingestion.
- External source management and event normalization.
- Risk assessment calculations and composite scoring.
- Historical risk analysis.
- Interactive frontend and geographic visualization.
- Travel advisory integration.
- Production deployment.

The existing geographic data pipeline provides a foundation for future ingestion systems but does not yet constitute a complete geopolitical data collection platform.

## REST API

WATCHtower currently includes five GET endpoints implemented using Flask Blueprints.

### State Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/states` | Retrieve all stored countries and areas |
| GET | `/api/states/<iso_code>` | Retrieve a country or area by ISO3 code |
| GET | `/api/states/<iso3>/events` | Retrieve events associated with a country or area |

### Event Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/events` | Retrieve all stored geopolitical events |
| GET | `/api/events/<event_id>` | Retrieve an individual event by its database ID |

### Example Requests

Retrieve all countries and areas:

```http
GET http://127.0.0.1:5000/api/states
```

Retrieve a country by ISO3 code:

```http
GET http://127.0.0.1:5000/api/states/USA
```

Retrieve events associated with a country:

```http
GET http://127.0.0.1:5000/api/states/UKR/events
```

Retrieve all events:

```http
GET http://127.0.0.1:5000/api/events
```

### Example State Response

```json
{
  "id": 1,
  "name": "Afghanistan",
  "iso3": "AFG"
}
```

The example above illustrates the current response structure; database IDs depend on the local database.

### API Behavior

- Successful GET requests return JSON with HTTP status `200`.
- Requests for nonexistent countries or events return HTTP status `404`.
- Country ISO3 lookups are case-insensitive.
- Event endpoints return empty JSON arrays when no matching events are stored.
- Event responses include geographic coordinates when available.

**Current limitation:** Event retrieval endpoints have been implemented, but the database does not yet contain an established external geopolitical event dataset. These endpoints require additional testing with populated event records.

## Database Architecture

WATCHtower uses **PostgreSQL** as its primary relational database, with **Flask-SQLAlchemy** providing object-relational mapping.

The backend defines five primary tables:

| Table | Purpose |
|---|---|
| `states` | Country and area identifiers and geographic information |
| `sources` | Information source metadata and attribution |
| `events` | Geopolitical events and developments |
| `risks` | Country-level geopolitical risk assessments |
| `risk_history` | Historical geopolitical risk records |

The initial database schema has been created successfully.

The `states` table contains 248 records retrieved from the United Nations M49 classification system. The remaining tables are currently unpopulated pending development of their associated functionality.

### Database Management

Database connectivity is configured through the `DATABASE_URL` environment variable.

The application currently initializes database tables using SQLAlchemy's `db.create_all()` functionality.

Flask-Migrate is included in the project's dependencies, but a version-controlled database migration workflow has not yet been established.

## Backend Architecture

WATCHtower separates backend responsibilities into distinct modules:

- **Models:** SQLAlchemy database model definitions.
- **Routes:** Flask Blueprints defining REST API endpoints.
- **Serializers:** Reusable functions for converting model objects into JSON-compatible dictionaries.
- **Ingestion:** Utilities for retrieving external data.
- **Seeding:** Scripts for populating database tables.
- **Data:** Locally stored geographic datasets.
- **Application Configuration:** Flask initialization and Blueprint registration.

This modular structure is intended to support future expansion without concentrating database models, endpoint logic, and data processing in a single file.

## Technology Stack

### Current Backend

- **Python:** Primary backend programming language.
- **Flask:** Web application framework.
- **Flask-SQLAlchemy:** Object-relational mapping and database integration.
- **PostgreSQL:** Relational database management system.
- **Psycopg:** PostgreSQL database driver.
- **Requests:** HTTP communication with external sources.
- **Beautiful Soup:** Parsing structured information from web resources.
- **python-dotenv:** Environment-based configuration.
- **Flask-Migrate:** Installed for future database migration management.

### Development Tools

- Git and GitHub
- PyCharm
- pgAdmin 4
- Python virtual environments

### Planned Components

- Automated geopolitical data ingestion pipelines.
- Interactive web frontend and geographic visualization.
- Country information dashboards.
- Risk assessment and historical analysis.
- Automated testing and monitoring.
- Production deployment infrastructure.
- Potential future desktop application using a shared frontend and backend API.

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

```bash
python -m pip install -r requirements.txt
```

### 4. Configure PostgreSQL

Create a local PostgreSQL database named:

```text
watchtower
```

Inside the `backend` directory, create a `.env` file containing:

```dotenv
DATABASE_URL=postgresql+psycopg://postgres:YOUR_PASSWORD@localhost:5432/watchtower
```

Replace `YOUR_PASSWORD` with your local PostgreSQL password and adjust the username, host, or port as necessary.

**Security:** The `.env` file is excluded from Git tracking. Never commit passwords, API keys, or other sensitive credentials.

### 5. Run the Backend

Navigate into the backend directory:

```bash
cd backend
```

Start the Flask development server:

```bash
python -m flask --app app run --debug
```

The application connects to PostgreSQL using `DATABASE_URL` and currently initializes its database tables through SQLAlchemy.

### 6. View Registered API Routes

To inspect the routes registered with Flask:

```bash
python -m flask --app app routes
```

This command lists the application's available endpoints and their supported HTTP methods.

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

### Seed the PostgreSQL Database

After configuring PostgreSQL and initializing the database, run:

```bash
python -m seeding.seed_states
```

The seeding utility reads the local JSON dataset and inserts country and area records into PostgreSQL.

The initial seeding process was successfully tested with:

```text
Added 248 states. Skipped 0 existing states.
```

The utility checks for existing records to avoid inserting duplicates during repeated execution.

### Verify Database Records

From the `backend` directory, run:

```powershell
python -c "from app import app; from models import State; ctx = app.app_context(); ctx.push(); print('Total states:', State.query.count()); ctx.pop()"
```

Expected output for the current dataset:

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
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── states.py
│   │   └── events.py
│   ├── seeding/
│   │   ├── __init__.py
│   │   ├── fetch_states.py
│   │   └── seed_states.py
│   └── serializers/
│       ├── __init__.py
│       ├── state_serializer.py
│       └── event_serializer.py
└── frontend/
```

The structure reflects the current backend organization and will expand as additional components are implemented.

Local environment configuration files and virtual environments are excluded from version control.

## Project Documentation

For a more detailed explanation of WATCHtower's objectives, intended functionality, and development scope, see:

[WATCHtower Project Overview and Objectives](DOCS/WATCHtower%20Project%20Overview%20and%20Objectives.pdf)

## Development Roadmap

WATCHtower is currently focused on backend infrastructure, geographic data management, and initial REST API functionality.

The following roadmap tracks individual development milestones rather than treating entire phases as complete.

### Phase 1 — Backend Architecture and Infrastructure

- [x] Establish initial Flask application.
- [x] Define core SQLAlchemy database models.
- [x] Configure PostgreSQL database connection.
- [x] Initialize initial relational database tables.
- [x] Configure environment-based database credentials.
- [x] Organize API endpoints using Flask Blueprints.
- [x] Introduce reusable model serializers.
- [ ] Establish version-controlled database schema migrations.
- [ ] Implement comprehensive input validation and error handling.
- [ ] Develop automated backend tests.

### Phase 2 — Geographic Data and Country Information

- [x] Implement initial UN M49 data retrieval.
- [x] Store retrieved country and area information in JSON.
- [x] Implement and test initial PostgreSQL state seeding.
- [x] Implement initial country retrieval API endpoints.
- [ ] Validate and refine country metadata.
- [ ] Expand country profiles with additional geographic, demographic, and political information.
- [ ] Establish periodic country data updates.

### Phase 3 — Geopolitical Data Collection

- [x] Implement initial event retrieval API endpoints.
- [ ] Test event endpoints with populated database records.
- [ ] Implement event pagination and filtering.
- [ ] Evaluate and select external geopolitical data providers.
- [ ] Implement source registration and metadata management.
- [ ] Develop initial geopolitical event ingestion pipeline.
- [ ] Normalize and validate incoming geopolitical event data.
- [ ] Associate ingested events with relevant countries and sources.
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
- [ ] Evaluate packaging the web frontend as a desktop application.

## Disclaimer

WATCHtower is an independent software development project intended for educational, informational, and analytical purposes.

Any future geopolitical risk indicators will represent descriptive assessments based on available data and should not be interpreted as predictions of future events, official intelligence assessments, or professional security recommendations.

## Author

**Matthew MacLean**

University of Florida — Computer Science

GitHub: https://github.com/MMacLean305