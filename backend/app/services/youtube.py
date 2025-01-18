from googleapiclient.discovery import build
from app.core.config import settings

class YouTubeService:
    def __init__(self):
        self.youtube = build("youtube", "v3", developerKey=settings.API_KEY)

    def search_videos(self, query: str, max_results: int = 5):
        request = self.youtube.search().list(
            part="snippet",
            q=query,
            maxResults=max_results
        )
        response = request.execute()
        return response

    def get_video_details(self, video_id: str):
        request = self.youtube.videos().list(
            part="snippet,statistics,contentDetails",
            id=video_id
        )
        response = request.execute()
        return response
