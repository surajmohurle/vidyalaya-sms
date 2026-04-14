# Vidyalaya - School Management System

Vidyalaya is a student management system built with FastAPI and SQLAlchemy. It provides a RESTful API for managing academic records and a minimalist administrative dashboard.

## Features

- **Authentication**: JWT-based login with Admin and Teacher roles.
- **Student Registry**: CRUD operations for student records, grades, and subjects.
- **Admin Dashboard**: Web interface for viewing and managing student data.
- **API Documentation**: Automatic Swagger and ReDoc documentation.
- **Deployment**: Support for Docker and Docker Compose.

## Installation

### Prerequisites
- Python 3.14+
- Docker (optional)

### Docker Deployment
```bash
docker-compose up -d
```
Access the dashboard at `http://localhost:8000/dashboard` and documentation at `http://localhost:8000/docs`.

### Local Setup
1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run database migrations:
   ```bash
   alembic upgrade head
   ```
4. Start the server:
   ```bash
   uvicorn app.main:app --reload
   ```

## API Access

Interactive documentation is available at:
- Swagger UI: `/docs`
- ReDoc: `/redoc`

## License
MIT