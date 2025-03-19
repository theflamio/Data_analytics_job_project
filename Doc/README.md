# Data Analytics Job Project

The **Data Analytics Job Project** is a containerized data pipeline designed to automate data extraction, transformation, loading (ETL), orchestration, and visualization. The project leverages **Docker Compose** to orchestrate four key containers, ensuring a modular and scalable architecture.

1. **ETL Container**: Fetches data from **Kaggle**, transforms it using **Python and Pandas**, and loads it into the **PostgreSQL** database.  
2. **PostgreSQL Container**: Serves as the data storage backend, maintaining processed and cleaned data for analysis.  
3. **Apache Superset Container**: Provides interactive data visualization and dashboarding by connecting directly to the PostgreSQL database.  
4. **Prefect Container**: Manages and orchestrates the ETL workflows, ensuring reliable and repeatable pipeline execution.  

The project also incorporates **CI/CD pipelines** using **GitHub Actions** for automated building, testing, and deployment of Docker containers. Built images are pushed to a **Docker Registry**, maintaining version control and facilitating rapid deployment.
