from fastapi import APIRouter
from routes.product import router as productRouter
from routes.user import router as userRouter

router =APIRouter(prefix="/api")
router.include_router(productRouter)
router.include_router(userRouter)
