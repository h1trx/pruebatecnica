from fastapi import APIRouter, status
from schemas.user import LoginSchema
from modules.user import User
from schemas.APIResponse import APIResponseSchema

router = APIRouter(prefix="/user", tags=["User"])

@router.post("/login")
def login(user: LoginSchema, status_code= status.HTTP_202_ACCEPTED):
    token = User.Login(user.id, user.psswd)
    return APIResponseSchema(
        status= "success",
        message= "Loggued",
        data= {
            "token": token
        }
    )