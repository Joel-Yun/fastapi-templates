from fastapi import APIRouter
from fastapi.responses import HTMLResponse

from routers.page.main import main_router

router = APIRouter(prefix="", default_response_class=HTMLResponse)

router.include_router(main_router.router, prefix="/")
