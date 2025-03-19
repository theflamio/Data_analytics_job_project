# Architecture

The **Data Analytics Job Project** architecture is designed to be fully containerized and orchestrated using **Docker Compose**. The architecture comprises four main containers, each with a specific role in the data pipeline:

## 1. ETL Container
- **Purpose:** Fetch, transform, and load data from Kaggle to the PostgreSQL database.
- **Technologies:** Python, Pandas.
- **Functions:**
  - Connects to the Kaggle API to download datasets.
  - Transforms data as needed using Pandas.
  - Loads the transformed data into PostgreSQL.
- **Scheduling:** Uses Prefect for automated and scheduled data processing.

## 2. PostgreSQL Container
- **Purpose:** Store transformed and cleaned data.
- **Technologies:** PostgreSQL 13+
- **Functions:**
  - Acts as a central data repository.
  - Supports data queries and connections from Superset.
- **Persistence:** Uses Docker volumes to retain data between container restarts.

## 3. Apache Superset Container
- **Purpose:** Visualize data and create interactive dashboards.
- **Technologies:** Apache Superset.
- **Functions:**
  - Connects directly to the PostgreSQL database.
  - Allows users to create, customize, and share dashboards.
- **Access:** Accessible via a web interface on localhost:8088.

## 4. Prefect Container
- **Purpose:** Orchestrate and monitor ETL workflows.
- **Technologies:** Prefect.
- **Functions:**
  - Automates and schedules ETL jobs.
  - Monitors workflow status and logs.
- **Access:** Accessible via a web interface on localhost:4200.

## Docker Compose
- **Orchestration:** Manages multi-container setups with dependency resolution.
- **Networking:** Creates an internal network for seamless inter-container communication.
- **Environment Configuration:** Uses environment variables for easy customization.
