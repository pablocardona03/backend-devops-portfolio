from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_logs():
    return {"message": "List of logs"}
