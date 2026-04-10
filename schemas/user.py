from pydantic import BaseModel

class LoginSchema(BaseModel):
    id: int
    psswd: int