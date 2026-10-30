# CloudOps Deployment Dashboard

A Python Flask web application designed to demonstrate application deployment and monitoring using Microsoft Azure.

## Technologies

- Python
- Flask
- Gunicorn
- HTML5
- CSS3
- Git and GitHub
- GitHub Actions
- Microsoft Azure App Service (planned)
- Terraform (planned)

## Features

- Application dashboard
- Application health-check endpoint
- Application information API
- Environment and version display
- Responsive dark-themed interface
- Automated unit tests
- GitHub Actions CI workflow

## Project Structure

```text
azure/
├── .github/
│   └── workflows/
│       └── ci.yml
├── static/
│   └── style.css
├── templates/
│   └── index.html
├── tests/
│   ├── __init__.py
│   └── test_app.py
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Run Locally

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it in Git Bash:

```bash
source .venv/Scripts/activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Start the application:

```bash
python app.py
```

Open http://127.0.0.1:5000 in your browser.

## API Endpoints

| Endpoint | Purpose |
|---|---|
| `/` | Main dashboard |
| `/health` | Application health check |
| `/api/info` | Application information |

## Run Automated Tests

```bash
python -m unittest discover -s tests -p "test*.py" -v
```

## CI Pipeline

The GitHub Actions workflow installs the dependencies and runs the automated unit tests on pushes and pull requests targeting the `main` branch.

## Azure Deployment Plan

The next phase is to provision Azure App Service infrastructure with Terraform and deploy the Python application directly to Azure App Service. Docker is not used in this project.
