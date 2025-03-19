# CI/CD

The CI/CD pipeline for the **Data Analytics Job Project** leverages **GitHub Actions** for continuous integration and delivery. This pipeline automates the building, testing, and deployment of the Docker containers, ensuring a smooth and consistent update process.

## Pipeline Overview
1. **Build and Test:** Automatically builds the Docker images for all containers when changes are pushed to the repository.
2. **Docker Registry Push:** Pushes the built images to a Docker Registry for version control and deployment.
3. **Deployment:** Pulls and deploys the latest images to the target environment.

## GitHub Actions Workflow
- **Trigger:** On every push or pull request to the `main` branch.
- **Jobs:**
  - **Build:** Uses Docker Compose to build images for all containers.
  - **Test:** Runs unit tests and integration tests to ensure pipeline integrity.
  - **Push to Registry:** Pushes images to Docker Hub or another registry.
  - **Deploy:** Updates the running containers on the target server.

## Docker Registry
- **Usage:** Stores and manages built container images.
- **Authentication:** Uses secure credentials stored in GitHub Secrets.
- **Tagging:** Images are tagged with the commit hash for traceability.

## Benefits
- **Automation:** Reduces manual effort and errors.
- **Consistency:** Maintains uniformity in the pipeline through automated testing and deployment.
- **Scalability:** Easily adapts to changes and updates without manual intervention.

