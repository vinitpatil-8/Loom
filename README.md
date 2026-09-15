# 🧠 Personal Life API

A personal REST API built with **Python, FastAPI, and Pydantic** to collect, manage, and eventually analyze data from my everyday life.

The goal is to build a central API for things like **study sessions, subjects, workouts, sleep, GitHub activity, and other personal data** — essentially creating a structured digital record of my life.

> 🚧 **Status:** Early development — currently experimenting with API design and CRUD operations.

---

## ✨ Current Features

* 📚 Create study records
* 🔍 Retrieve all study records
* 🎯 Retrieve study data for a specific day
* ✏️ Update existing study records
* 🗑️ Delete study records
* ✅ Request validation using Pydantic
* 📖 Automatic interactive API documentation with FastAPI

---

## 🛠️ Tech Stack

* **Python** — Programming language
* **FastAPI** — REST API framework
* **Pydantic** — Data validation and schemas
* **Uvicorn** — ASGI server

### Planned

* **SQLAlchemy** — Database ORM
* **SQLite** — Development database
* **PostgreSQL** — Production database
* **APIRouter** — Modular API organization
* **React + TypeScript** — Frontend dashboard
* **GitHub API** — Automatic GitHub activity tracking

---

## 📂 Project Structure

The project is being developed toward a modular structure like:

```text
personal-life-api/
│
├── main.py
│
├── routers/
│   ├── study.py
│   └── subjects.py
│
├── models/
│
├── schemas/
│
├── database.py
│
└── requirements.txt
```

The structure will evolve as more features are added.

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone <repository-url>
cd personal-life-api
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

**Windows:**

```bash
venv\Scripts\activate
```

**macOS / Linux:**

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Start the development server

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

---

## 📖 API Documentation

FastAPI automatically generates interactive API documentation.

Once the server is running, open:

```text
http://127.0.0.1:8000/docs
```

You can use this page to test endpoints directly without building a frontend.

An alternative documentation interface is available at:

```text
http://127.0.0.1:8000/redoc
```

---

## 🔌 API Endpoints

### Study

| Method   | Endpoint       | Description                       |
| -------- | -------------- | --------------------------------- |
| `GET`    | `/study`       | Get all study records             |
| `GET`    | `/study/{day}` | Get study data for a specific day |
| `POST`   | `/study`       | Create a study record             |
| `PUT`    | `/study/{id}`  | Update a study record             |
| `DELETE` | `/study/{id}`  | Delete a study record             |

### Example Study Data

```json
{
  "day": 15,
  "subject": "DSA",
  "time": 2
}
```

---

## 🧩 How It Works

The basic API flow is:

```text
Client
  │
  │ HTTP Request
  ▼
FastAPI
  │
  │ Validate data
  ▼
Pydantic
  │
  │ Application logic
  ▼
Database
  │
  │ Response
  ▼
FastAPI
  │
  │ JSON
  ▼
Client
```

Currently, study data is stored in memory while the API is being developed.

The next major step is replacing in-memory storage with a persistent database using **SQLAlchemy**.

---

## 🗺️ Roadmap

### Phase 1 — API Fundamentals

* [x] Create FastAPI application
* [x] Create GET endpoints
* [x] Create POST endpoints
* [x] Create PUT endpoints
* [x] Create DELETE endpoints
* [x] Use Pydantic models
* [ ] Improve error handling
* [ ] Improve HTTP status codes
* [ ] Refactor endpoints using `APIRouter`

### Phase 2 — Database

* [ ] Learn SQLAlchemy
* [ ] Design database models
* [ ] Connect SQLite
* [ ] Replace in-memory storage
* [ ] Implement database CRUD
* [ ] Add relationships between entities

### Phase 3 — Expand LifeBase

* [ ] Study tracking
* [ ] Subject tracking
* [ ] Workout tracking
* [ ] Sleep tracking
* [ ] Reading tracking
* [ ] Daily activity tracking

### Phase 4 — External Data

* [ ] GitHub API integration
