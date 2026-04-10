from pydantic import BaseModel
from typing import Literal, TypeVar

T = TypeVar("T")

class APIResponseSchema(BaseModel):
    status: Literal["success", "failed"]
    message: str
    data: T