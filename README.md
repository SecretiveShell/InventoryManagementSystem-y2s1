# InventoryManagementSystem-y2s1

An inventory management system designed as part of the SWQ course at university.

## technologies used

### Backend

- FastAPI
- SQLAlchemy
- Redis
- Pydantic
- postgreSQL

### Frontend

- html
- css
- javascript

## Installation

to install this app either use the dev containers to create a test environment or use docker compose to build the containers

To run the full stack, including the backend and frontend, run `./start.sh` or execute the following commands:

```bash
uvicorn main:app --reload --app-dir backend/src
caddy run
```

This will start the backend server and caddy server, allowing you to view and interact with the frontend application in your web browser.

## Testing

| Type               | Tool                      |
| ------------------ | ------------------------- |
| Unit Testing       | pytest                    |
| accessibility      | lighthouse                |
| linting/formatting | ruff (with github action) |
| load testing       | Jmeter                    |
| Security           | OWASP Zap                 |
