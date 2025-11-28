from fastapi import APIRouter


# NOTE: '/api/ping' path에 대한 라우터
router = APIRouter(prefix="/ping")


# NOTE: Ping/Pong 테스트
@router.get("")
async def ping():
    return {"message": "pong"}
