import os
import logging
from functools import lru_cache

from common.configs.core.config_loader import get_configs


def init_logger() -> logging.Logger:
    """
    NOTE: 로거 초기화
    """

    # NOTE: 설정 로드
    configs = get_configs()

    log_file_path = configs.LOGGER.LOG_FILE_PATH
    log_folder_path = os.path.dirname(log_file_path)

    # NOTE: 로그 폴더 생성
    os.makedirs(log_folder_path, exist_ok=True)

    # NOTE: 로깅 설정
    logging.basicConfig(
        # NOTE: 로그 레벨 설정
        level=configs.LOGGER.LOG_LEVEL,
        # NOTE: 포맷 지정
        format="[%(levelname)s] %(asctime)s - %(message)s",
        # NOTE: 핸들러 지정
        handlers=[
            # NOTE: 터미널 출력
            logging.StreamHandler(),
            # NOTE: 파일 저장
            logging.FileHandler(log_file_path, mode="a"),
        ],
    )

    # NOTE: 로거 가져오기
    logger = logging.getLogger("fastapi_app")

    return logger


@lru_cache()
def get_logger() -> logging.Logger:
    """
    NOTE: 로거 인스턴스 반환 함수
    """
    return init_logger()
