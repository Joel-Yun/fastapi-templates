from fastapi.requests import Request
from core.templates import templates

from datetime import datetime


# Main page view function
def main_page(req: Request):
    now = datetime.now()

    return templates.TemplateResponse(
        req, "main_template.jinja", {"date": now.strftime("%Y-%m-%d %H:%M:%S")}
    )
