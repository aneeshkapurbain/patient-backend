from pydantic import BaseModel
from typing import Any


class Generic(BaseModel):
    status_code: int
    message: str
    data: Any
