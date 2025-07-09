from fastapi import APIRouter

from routers.api.ping import ping_router

# NOTE: '/api'
api_router = APIRouter(prefix="/api")

api_router.include_router(ping_router.router)
