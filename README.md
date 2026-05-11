# 🚀 Task Management API FastAPI-backend

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

# 🐘 Install & Start PostgreSQL

## macOS (Homebrew)

```bash
brew install postgresql@17
```

Add to PATH:

```bash
export PATH="/opt/homebrew/opt/postgresql@17/bin:$PATH"
```

Start PostgreSQL service:

```bash
brew services start postgresql@17
```

Verify:

```bash
psql --version
```

## Windows

Download and install from: https://www.postgresql.org/download/windows/

Start PostgreSQL service:

```powershell
net start postgresql-x64-17
```

## Create Database

```bash
psql -U postgres
```

```sql
CREATE DATABASE taskdb;
```

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

## 2️⃣ Initialize Project

```bash
uv init
```

---

## 3️⃣ Create Virtual Environment

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

## 4️⃣ Add FastAPI

```bash
uv add fastapi[standard]
```

---

## 5️⃣ Add Required Packages

```bash
uv add sqlalchemy alembic psycopg2-binary python-jose[cryptography] passlib[bcrypt] python-dotenv
```

---

## 6️⃣ Install Dependencies

```bash
uv sync
```

---

## 7️⃣ Setup Environment Variables

Create `.env` file in the root directory:

```env
APP_NAME=Task API
DEBUG=True
DATABASE_URL=postgresql://postgres:password@localhost:5432/taskdb
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## 8️⃣ Run Database Migrations

```bash
uv run alembic upgrade head
```

---

## 9️⃣ Run Application

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

---

# 🎤 Interview Preparation

## What is this project?

"I built a **Task Management REST API** using **FastAPI** — a modern Python web framework. It allows users to register, login, and manage their tasks with full CRUD operations."

---

## Tech Stack — How to explain each

- **FastAPI** — "I used FastAPI because it's fast, async-ready, and auto-generates Swagger docs at `/docs`"
- **PostgreSQL** — "Relational database to store users and tasks"
- **SQLAlchemy** — "ORM to interact with the database using Python classes instead of raw SQL"
- **Alembic** — "Database migration tool — when I change a model, I run a migration to update the DB schema"
- **JWT** — "JSON Web Token for authentication — user logs in, gets a token, and sends it with every request"
- **Docker** — "Containerized the app so it runs the same on any machine"
- **UV** — "Modern Python package manager, faster than pip"

---

## Architecture — How to explain

"I followed **clean architecture** — each layer has one responsibility:"

```
routes      → handles HTTP requests
controller  → business logic
models      → database tables
schemas     → request/response validation (Pydantic)
repositories → database queries
```

---

## Controller Code — How to explain

"For example, in my `create_task` function:"

```python
def create_task(body: TaskSchema, db: Session, user: UserModel):
    new_task = TaskModel(...)
    db.add(new_task)
    db.commit()
```

"I take validated input from `TaskSchema`, create a `TaskModel` object, save it to the DB, and return a standard API response."

---

## Common Interview Questions

**Q: Why FastAPI over Flask/Django?**
"FastAPI is faster, has built-in data validation via Pydantic, and auto-generates API docs."

**Q: How does JWT work here?**
"User logs in → server generates a signed token → client sends token in `Authorization: Bearer <token>` header → server verifies it on each request."

**Q: What is Alembic?**
"It tracks changes to SQLAlchemy models and generates SQL migration scripts automatically."

**Q: What is dependency injection in FastAPI?**
"FastAPI's `Depends()` injects things like `db: Session` or the current `user` into route handlers automatically."
