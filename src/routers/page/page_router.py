from fastapi import APIRouter
from fastapi.responses import HTMLResponse

from routers.page.main import main_router

page_router = APIRouter(default_response_class=HTMLResponse)

page_router.include_router(main_router.router)
