# FastAPI-backend


# 🚀 Task Management API

A scalable task management backend built using FastAPI and UV.

---

# 📌 Features

- FastAPI REST API
- JWT Authentication
- Task CRUD Operations
- PostgreSQL Database
- SQLAlchemy ORM
- Alembic Migration
- Docker Support
- Clean Architecture
- Environment Config
- Swagger Documentation
- UV Package Manager

---

# 🛠 Tech Stack

| Technology | Usage |
|------------|-------|
| FastAPI | Backend Framework |
| UV | Python Package Manager |
| PostgreSQL | Database |
| SQLAlchemy | ORM |
| Alembic | Database Migration |
| JWT | Authentication |
| Docker | Containerization |

---

# 📂 Project Structure

```bash
backend/
│
├── app/
│   ├── api/
│   │   ├── routes/
│   │   └── dependencies/
│   │
│   ├── core/
│   │   ├── config.py
│   │   ├── database.py
│   │   └── security.py
│   │
│   ├── models/
│   ├── schemas/
│   ├── repositories/
│   ├── services/
│   ├── middleware/
│   ├── utils/
│   └── main.py
│
├── tests/
├── alembic/
├── pyproject.toml
├── uv.lock
├── Dockerfile
├── docker-compose.yml
└── .env
```

---

# ⚙️ Prerequisites

Install:

- Python 3.12+
- UV
- PostgreSQL

---

# 📦 Install UV

## macOS / Linux

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Windows

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Verify installation:

```bash
uv --version
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/task-management-api.git
cd task-management-api
```

---

## 2️⃣ Create Virtual Environment

```bash
uv venv
```

Activate environment:

### macOS / Linux

```bash
source .venv/bin/activate
```

### Windows

```powershell
.venv\Scripts\activate
```

---

## 3️⃣ Install Dependencies

```bash
uv sync
```

---

# 🔐 Environment Variables

Create `.env`

```env
APP_NAME=Task API

DEBUG=True

DATABASE_URL=postgresql://postgres:password@localhost:5432/taskdb

SECRET_KEY=your_secret_key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

# ▶️ Run Application

## Development Server

```bash
uv run uvicorn app.main:app --reload
```

Application URL:

```text
http://127.0.0.1:8000
```

---

# 📚 API Documentation

| Type | URL |
|------|-----|
| Swagger UI | `/docs` |
| ReDoc | `/redoc` |

Example:

```text
http://127.0.0.1:8000/docs
```

---

# 🗄 Database Migration

## Create Migration

```bash
uv run alembic revision --autogenerate -m "Initial migration"
```

## Apply Migration

```bash
uv run alembic upgrade head
```

---

# 🧪 Running Tests

```bash
uv run pytest
```

---

# 🐳 Docker Setup

## Build & Run

```bash
docker-compose up --build
```

---

# 🌿 Git Branch Strategy

| Branch | Purpose |
|--------|---------|
| main | Production |
| develop | Development |
| feature/* | New Features |
| bugfix/* | Bug Fixes |

Example:

```bash
feature/auth-system
feature/task-module
```

---

# 🚀 Deployment

Supported Platforms:

- AWS EC2
- DigitalOcean
- Render
- Railway
- VPS with Docker

---

# 📌 Common UV Commands

| Command | Description |
|--------|-------------|
| `uv sync` | Install dependencies |
| `uv add package-name` | Add package |
| `uv remove package-name` | Remove package |
| `uv run command` | Run command |
| `uv lock` | Update lock file |

---

# 🤝 Contributing

1. Fork Repository
2. Create Feature Branch
3. Commit Changes
4. Push Changes
5. Open Pull Request

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

Your Name  
Your Company

---

# ⭐ Support

If you like this project, give it a ⭐ on GitHub.
