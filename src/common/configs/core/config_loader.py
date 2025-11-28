import json
from pathlib import Path
from pathlib import Path
from functools import lru_cache
from pydantic_settings import BaseSettings

from common.configs.schemas.logger_schema import LoggerSchema


class Configs(BaseSettings):
    """
    NOTE: config.json 파일에서 설정을 로드하고 검증하는 Pydantic 모델 클래스
    """

    # NOTE: 각 컨픽의 기본 값 설정
    LOGGER: LoggerSchema = LoggerSchema()

    def __init__(self):
        # NOTE: 프로젝트 루트의 configs/config.json 파일 경로 설정
        config_path = Path.cwd() / "configs" / "config.json"

        # NOTE: config.json 파일에서 설정을 로드
        try:
            with open(config_path, "r", encoding="utf-8") as f:
                config_data = json.load(f)
                super().__init__(**config_data)
        except Exception as e:
            print(f"Could not load config from {config_path}: {e}")
            raise e


@lru_cache()
def get_configs() -> Configs:
    """
    NOTE: Configs 클래스 인스턴스 반환 함수
    """
    return Configs()
