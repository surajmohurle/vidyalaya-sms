# 🏫 Vidyalaya - Smart School Management System

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

**Vidyalaya** is a production-ready Student Management System built with a focus on speed, security, and professional administrative workflows. It transforms school operations into a streamlined, digital experience.

---

## ✨ Key Features

- **🛡️ Secure Authentication**: JWT-based authentication with distinct Role-Based Access Control (RBAC) for Admins and Teachers.
- **📊 Admin Dashboard**: A clean, minimalist web interface for managing student registries without the clutter of traditional systems.
- **🔗 Standardized API**: Fully documented RESTful API endpoints with consistent response envelopes and error handling.
- **🚀 Zero-Setup Deployment**: Orchestrated with Docker and Docker Compose for one-command deployment.
- **📋 Student Registry**: Comprehensive management of students, grades, subjects, and registration history.

---

## 🛠️ Technical Stack

- **Backend**: [FastAPI](https://fastapi.tiangolo.com/) (Python 3.14 compatible)
- **ORM**: [SQLAlchemy](https://www.sqlalchemy.org/) with [Alembic](https://alembic.sqlalchemy.org/) for migrations
- **Security**: Bcrypt password hashing & JOSE (JWT) token management
- **Frontend**: Vanilla JavaScript and CSS (Modern, minimalist aesthetic)
- **Database**: SQLite (Default for zero-setup), configurable to PostgreSQL
- **Containerization**: Docker & Docker Compose

---

## 🚀 Getting Started

### 📦 Using Docker (Recommended)
Launch the entire system in seconds:
```bash
docker-compose up -d
```
Access the dashboard at `http://localhost:8000/dashboard` and documentation at `http://localhost:8000/docs`.

### 🐍 Local Development
1. **Initialize Environment**:
   ```bash
   py -m venv venv
   .\venv\Scripts\activate
   ```
2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run Migrations**:
   ```bash
   alembic upgrade head
   ```
4. **Start Server**:
   ```bash
   uvicorn app.main:app --reload
   ```

---

## 📖 API Documentation

Once the server is running, explore the interactive documentation powered by Swagger UI:
- **Interactive Docs**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **Alternatice Docs**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🤝 Contribution & Portfolio

This project is part of my professional engineering portfolio. It demonstrates advanced concepts in:
- API design and dependency injection
- Secure authentication flows and encryption
- Database modeling and migration management
- Containerized deployment and CI/CD ready infrastructure

Developed by **Suraj Mohurle**. ✨