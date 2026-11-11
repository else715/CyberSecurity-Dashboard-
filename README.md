# Cybersecurity Dashboard

A small Flask and SQLite dashboard prototype for displaying stored security logs and threat records. The interface includes a log table and Chart.js visualization, while Flask serves the page and JSON endpoints.

> **Project status:** This is a learning/demo project. It does not include a live log collector or threat-detection pipeline. The checked-in database and sample UI are not production monitoring.

## Features

- Flask dashboard with a security log table and Chart.js visualization
- SQLite-backed log and threat records
- JSON endpoints at `/api/logs` and `/api/threats`

## Run locally

Requires Python 3 and Flask. From the repository root:

```bash
git clone https://github.com/else715/CyberSecurity-Dashboard-.git
cd CyberSecurity-Dashboard-/backend
python -m venv .venv
```

Activate the virtual environment, then install Flask and start the app:

```bash
python -m pip install Flask
python app.py
```

Open `http://127.0.0.1:5000` in your browser. The app currently uses Flask debug mode; keep it on a local development machine and do not expose it to the internet.

## Data

The dashboard reads records from SQLite. The JSON endpoints expose the stored data; the repository does not include an ingestion service that continuously collects logs. Review the database schema and application routes before adapting the prototype.
