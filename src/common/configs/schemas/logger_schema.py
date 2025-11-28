from pydantic import BaseModel


class LoggerSchema(BaseModel):
    """
    NOTE: 로거 설정 스키마 클래스
    """

    # NOTE: 로그 파일 경로
    LOG_FILE_PATH: str = ""

    # NOTE: 로그 레벨
    LOG_LEVEL: str = ""
