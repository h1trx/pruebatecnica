from fastapi import FastAPI, status, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from modules.authentication import authentication
from routes.router import router
from modules.user import User
from core.exceptions import (
    validation_exception_handler,
    http_exception_handler,
    general_exception_handler,
)

app = FastAPI()
app.include_router(router)

@app.get('/')
@authentication
async def root():
    #result = conn.execute(users.select().fetch())
    print("Hello")
    return "Root"

@app.get("/login")
def login():    
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "status": "success",
            "message": "Pague Loggin",
            "data": {}
        }
    )

app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(Exception, general_exception_handler)
