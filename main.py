from fastapi import FastAPI, status, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from modules.authentication import authentication
from routes.router import router
from config.db import conn, engine
from models.user import User
from sqlalchemy import select
from core.exceptions import (
    validation_exception_handler,
    http_exception_handler,
    general_exception_handler,
)

from sqlalchemy.ext.asyncio import async_sessionmaker

SessionLocal = async_sessionmaker(engine, expire_on_commit=False)

app = FastAPI()
app.include_router(router)

@app.get('/')
@authentication
async def root():
    async with SessionLocal() as session:
        result = await session.execute(select(User))
        tmp = result.scalars().all()
        print(tmp)
    return "Hello"

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
