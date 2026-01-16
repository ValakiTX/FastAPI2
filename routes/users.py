from fastapi import APIRouter, HTTPException
from typing import List

from models.user import User, User_Response


router = APIRouter()

# Sample data store
users_db: List[User] = [
    User(id=1, username="johndoe", email="john@example.com", full_name="John Doe"),
    User(id=2, username="janedoe", email="jane@example.com", full_name="Jane Doe", is_active=False),
]


@router.get("/", response_model=List[User_Response])
def get_all_users():
    """Return all users."""
    return users_db


@router.post("/", response_model=User_Response, status_code=201)
def create_user(user: User):
    """Create a new user."""
    for existing_user in users_db:
        if existing_user.id == user.id:
            raise HTTPException(status_code=400, detail="User with this ID already exists")
    users_db.append(user)
    return user


@router.get("/{id}", response_model=User)
def get_user_by_id(id: int):
    """Return a full user by ID."""
    for user in users_db:
        if user.id == id:
            return user
    raise HTTPException(status_code=404, detail="User not found")


@router.delete("/{id}", status_code=204)
def delete_user(id: int):
    """Remove user by ID."""
    for index, user in enumerate(users_db):
        if user.id == id:
            users_db.pop(index)
            return
    raise HTTPException(status_code=404, detail="User not found")
