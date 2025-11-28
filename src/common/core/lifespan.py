from fastapi import FastAPI
from contextlib import asynccontextmanager

from common.utils.logger import init_logger


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    NOTE: 애플리케이션 시작/종료 시 실행할 작업을 정의합니다.
    """

    # NOTE: 로거 초기화
    logger = init_logger()

    # NOTE: 애플리케이션 시작 시 실행할 작업
    logger.info("Starting application...")

    logger.info("Application started successfully.")

    yield

    # NOTE: 애플리케이션 종료 시 실행할 작업
    logger.info("Shutting down application...")

    # NOTE: something

    logger.info("Application shutdown complete.")
