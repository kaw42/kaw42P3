# Project Setup

[![Production Workflow 1](https://github.com/kaw42/kaw42P3/actions/workflows/prod.yml/badge.svg)](https://github.com/kaw42/kaw42P3/actions/workflows/prod.yml)
* [Production Deployment](https://kwilliam-prod.herokuapp.com/)


[![Development Workflow 3.8](https://github.com/kaw42/kaw42P3/actions/workflows/dev.yml/badge.svg)](https://github.com/kaw42/kaw42P3/actions/workflows/dev.yml)* [Developmental Deployment](https://kwilliam-dev.herokuapp.com/)

## Running Locally

1. To Build with docker compose:
   docker compose up --build
2. To run tests, Lint, and Coverage report use this command: pytest --pylint --cov

.pylintrc is the config for pylint, .coveragerc is the config for coverage and setup.py is a config file for pytest
