from fastapi import APIRouter

from routers.api.ping import ping_router


# NOTE: '/api' path에 대한 라우터
router = APIRouter(prefix="/api")

# NOTE: 서브 라우터 등록
router.include_router(ping_router.router)
