from pydantic import BaseModel, Field, field_validator
from typing import Optional
import re


class User(BaseModel):
    id: int
    username: str = Field(..., min_length=3, max_length=50)
    email: str
    full_name: Optional[str] = Field(default=None, max_length=100)
    is_active: bool = True

    @field_validator("email")
    @classmethod
    def validate_email(cls, v: str) -> str:
        email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if not re.match(email_pattern, v):
            raise ValueError("Invalid email format")
        return v


class User_Response(BaseModel):
    id: int
    full_name: Optional[str] = None
