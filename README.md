# FastAPI Modular Application

A modular FastAPI application demonstrating RESTful API design with Pydantic models, validation, and organized router structure.

## Project Structure

```
fastapi2/
├── main.py              # FastAPI application entry point
├── models/
│   ├── item.py          # Item and Item_Response models
│   └── user.py          # User and User_Response models with validation
├── routes/
│   ├── items.py         # Item retrieval endpoints
│   └── users.py         # User CRUD endpoints
├── requirements.txt     # Project dependencies
└── README.md
```

## Features

- **Pydantic Models** with validation (email regex, field length constraints)
- **Response Models** for controlling exposed data (`Item_Response`, `User_Response`)
- **Modular Routers** for organized endpoint management
- **CRUD Operations** for user management
- **HTTP Exception Handling** (404, 400 status codes)

## Installation

1. Activate the virtual environment:
   ```powershell
   .\Scripts\Activate.ps1
   ```

2. Install dependencies:
   ```bash
   pip install fastapi uvicorn pydantic[email]
   ```

## Running the Application

```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`

## API Endpoints

### Root
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | `/`      | Welcome message |

### Items
| Method | Endpoint      | Description           |
|--------|---------------|-----------------------|
| GET    | `/items/`     | List all items        |
| GET    | `/items/{id}` | Get item by ID        |

### Users
| Method | Endpoint       | Description                |
|--------|----------------|----------------------------|
| GET    | `/users/`      | List all users             |
| POST   | `/users/`      | Create a new user          |
| GET    | `/users/{id}`  | Get user by ID (full data) |
| DELETE | `/users/{id}`  | Delete user by ID          |

## API Documentation

FastAPI provides automatic interactive documentation:

- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

## Models

### Item
- `id`: int
- `name`: str
- `description`: str (optional)
- `price`: float

### User
- `id`: int
- `username`: str (3-50 characters)
- `email`: str (validated email format)
- `full_name`: str (optional, max 100 characters)
- `is_active`: bool (default: True)
