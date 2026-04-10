from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from schemas.APIResponse import APIResponseSchema

async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = [
        {
            "details": err["msg"],
            "field": err["loc"][-1]
        }
        for err in exc.errors()
    ]

    return JSONResponse(
        status_code=422,
        content=APIResponseSchema(
            status= "failed",
            message= "Error de validación",
            data= errors
        ).model_dump()
    )

async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content=APIResponseSchema(
            status= "failed",
            message= exc.detail,
            data= {}
        ).model_dump()
    )

async def general_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content=APIResponseSchema(
            status= "failed",
            message= "Error interno del servidor",
            data= {
                "details": str(exc)
            }
        ).model_dump()
    )
