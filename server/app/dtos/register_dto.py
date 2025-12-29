from pydantic import BaseModel, EmailStr, Field
from typing import Optional, Literal

class RegisterDTO(BaseModel):
    full_name: str = Field(..., min_length=1)
    email: EmailStr
    password: str = Field(..., min_length=8)

    user_type: Optional[Literal['user', 'admin']] = 'user'