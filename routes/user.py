from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from schemas.user import LoginSchema
from modules.user import User

router = APIRouter(prefix="/user", tags=["User"])

@router.post("/login")
def login(user: LoginSchema):
    token = User.Login(user.id, user.psswd)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "message": "Loggued",
            "token": token
        }
    )