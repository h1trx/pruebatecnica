from fastapi import APIRouter

router = APIRouter(prefix="/product")

@router.get("/")
def product():
    return "Hola"
