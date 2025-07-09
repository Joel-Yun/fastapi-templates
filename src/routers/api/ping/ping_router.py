from fastapi import APIRouter

# NOTE: '/api/ping'
router = APIRouter(prefix="/ping")


# NOTE: Ping/Pong 테스트
@router.get("/")
async def ping():
    return {"message": "pong"}
