from fastapi import APIRouter, Query
from app.services.youtube import YouTubeService

router = APIRouter()

@router.get("/")
async def search_channels(query: str = Query(...), max_results: int = Query(5)):
    youtube_service = YouTubeService()
    return youtube_service.search_channels(query, max_results)
