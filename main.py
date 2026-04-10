import models
from fastapi import FastAPI, status, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from modules.authentication import authentication
from routes.router import router
from config.db import engine
from config.base import Base
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
    return "Hello"

@app.get('/db')
async def db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

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
