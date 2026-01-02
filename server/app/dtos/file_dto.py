from pydantic import BaseModel, Field
from typing import Optional

class FileDTO(BaseModel):
    filename: str = Field(..., min_length=1, description="The name of the file")
    file_size: int = Field(..., gt=0)
    mime_type: str = Field(..., min_length=1)