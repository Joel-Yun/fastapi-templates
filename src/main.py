from fastapi import FastAPI

from routers.api import api_router
from common.core.lifespan import lifespan
from common.middlewares.request_logging_middleware import RequestLoggingMiddleware


# NOTE: 애플리케이션 인스턴스
app = FastAPI(
    docs_url=None,  # NOTE: API docs 제거
    redoc_url=None,  # NOTE: API docs 제거
    lifespan=lifespan,  # NOTE: 애플리케이션 시작/종료 시 실행할 작업 설정
)

# NOTE: 미들웨어 등록
app.add_middleware(RequestLoggingMiddleware)

# NOTE: 라우터 등록
app.include_router(api_router.router)
