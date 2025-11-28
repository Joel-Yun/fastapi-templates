from fastapi import Request
from starlette.responses import Response
from starlette.middleware.base import BaseHTTPMiddleware

from common.utils.logger import get_logger


class RequestLoggingMiddleware(BaseHTTPMiddleware):
    """
    NOTE: 요청 로깅 미들웨어
    """

    def __init__(self, app):
        super().__init__(app)
        self.logger = get_logger()

    async def dispatch(self, request: Request, call_next) -> Response:
        try:
            response = await call_next(request)

            client_host = request.client.host if request.client else "unknown"
            client_port = request.client.port if request.client else "unknown"
            http_version = request.scope.get("http_version", "1.1")

            # NOTE: 요청 정보 로깅
            self.logger.info(
                f'{client_host}:{client_port} - "{request.method} {request.url.path} HTTP/{http_version}" {response.status_code}'
            )

            return response

        except Exception as e:
            self.logger.error(f"Request Failed: {str(e)}")
            raise e
