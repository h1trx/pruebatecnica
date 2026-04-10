from fastapi import HTTPException, status
from fastapi.responses import JSONResponse

class User:
    
    def Login(id: int, psswd: int):
        if id != 31 or psswd != 31:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail= "Usuario incorrecto"
                )
        
        token = "jsissododododd"
        return token