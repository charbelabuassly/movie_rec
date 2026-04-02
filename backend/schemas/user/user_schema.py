from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    user_id: int
    user_name: str
    user_email: str
    is_deleted: bool = False

    class Config:
        from_attributes = True
