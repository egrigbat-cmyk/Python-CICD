Python CI/CD

A FastAPI application demonstrating automated testing, Docker-based CI/CD with GitHub Actions, and AWS container image delivery.

Overview

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

API Endpoints

Health Check

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

CI/CD Pipeline

The GitHub Actions workflow:

1. Checks out the repository.
2. Installs Python dependencies.
3. Runs automated tests using Pytest.
4. Builds the Docker image.
5. Authenticates to AWS using OIDC.
6. Pushes the Docker image to Amazon ECR.

Images are published to the python-cicd ECR repository in the eu-north-1 region.

Docker

Build the image:

docker build -t python-cicd .

Run the container:

docker run -p 8000:8000 python-cicd

Test the health endpoint:

curl http://127.0.0.1:8000/health

Run Locally

Install dependencies:

pip install -r requirements.txt

Start the application:

uvicorn main:app --reload

Run tests:

pytest

AWS Deployment

GitHub Actions uses AWS IAM OIDC authentication to obtain temporary credentials and publish Docker images to Amazon ECR without storing long-lived AWS access keys in GitHub secrets.

Current stage: Automated testing, Docker builds, and image publishing to Amazon ECR.

Next stage: Deploy the container to Amazon ECS Fargate and configure the service to run the application.

Project Structure

Python-CICD/
├── .github/
│   └── workflows/
│       └── ci.yml
├── main.py
├── test_main.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
└── README.md
