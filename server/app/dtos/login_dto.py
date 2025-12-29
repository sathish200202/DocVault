from pydantic import BaseModel, EmailStr, Field
from typing import Optional, Literal

class LoginDTO(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8)