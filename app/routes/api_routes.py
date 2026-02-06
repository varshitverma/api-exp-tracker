from fastapi import APIRouter

from app.routes.get_routes import router as get_routers
from app.routes.post_routes import router as post_routers
from app.routes.delete_routes import router as delete_routers

api_router = APIRouter()

api_router.include_router(get_routers)
api_router.include_router(post_routers)
api_router.include_router(delete_routers)