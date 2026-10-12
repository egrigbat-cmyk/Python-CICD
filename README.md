# Python CI/CD

A FastAPI application demonstrating automated testing, Docker-based CI/CD with GitHub Actions, and AWS container image delivery.

## Overview

This project is a small deployment health API built with Python and FastAPI.

It exposes health and version endpoints and uses automated tests and Docker builds to demonstrate a CI/CD workflow. GitHub Actions authenticates to AWS using OIDC and pushes the Docker image to Amazon ECR. Amazon ECS Fargate is the planned next step for running the application.

Tech Stack

* Python
* FastAPI
* Pytest
* Docker
* GitHub Actions
* AWS IAM (OIDC)
* Amazon ECR
* Amazon ECS Fargate
* Git

## API Endpoints

### Health Check

'''http

GET /health

Response:

{
  "status": "healthy"
}

Version

GET /version

Response:

{
  "application": "Deployment Health API",
  "version": "1.0.0"
}

## CI/CD Pipeline

The GitHub Actions workflow:

1. Checks out the repository.
2. Installs Python dependencies.
3. Runs automated tests using Pytest.
4. Builds the Docker image.
5. Authenticates to AWS using OIDC.
6. Pushes the Docker image to Amazon ECR.

Current stage: Automated testing, Docker builds, and image publishing to Amazon ECR.

Next stage: Deploy the container to Amazon ECS Fargate and configure the service to run the application.
