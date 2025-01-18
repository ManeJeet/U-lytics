from fastapi import APIRouter
from app.services.youtube import YouTubeService

router = APIRouter()

@router.get("/{video_id}")
async def get_video_details(video_id: str):
    youtube_service = YouTubeService()
    return youtube_service.get_video_details(video_id)
