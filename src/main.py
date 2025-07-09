from fastapi import FastAPI

from routers.api.api_router import api_router
from routers.page.page_router import page_router

# Application instance
app = FastAPI()

app.include_router(api_router)
app.include_router(page_router)
