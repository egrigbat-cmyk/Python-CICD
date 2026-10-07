# Python CI/CD

A simple FastAPI application demonstrating automated testing and Docker-based CI/CD with GitHub Actions.

## Overview

This project is a small deployment health API built with Python and FastAPI.

It exposes health and version endpoints and uses automated tests and Docker builds to demonstrate a basic CI/CD workflow.

## Tech Stack

- Python
- FastAPI
- Pytest
- Docker
- GitHub Actions
- Git

## API Endpoints

### Health Check

```http

GET /health

{
  "status": "healthy"
}

GET /version

{
  "application": "Deployment Health API",
  "version": "1.0.0"
}
