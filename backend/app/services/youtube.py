from googleapiclient.discovery import build
from app.core.config import settings

class YouTubeService:
    def __init__(self):
        self.youtube = build("youtube", "v3", developerKey=settings.API_KEY)

    def search_videos(self, query: str, max_results: int = 5):
        request = self.youtube.search().list(
            part="snippet",
            q=query,
            maxResults=max_results,
            type="video"
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

    # ------------------------
    # New methods for playlists and channels
    # ------------------------
    def search_playlists(self, query: str, max_results: int = 5):
        request = self.youtube.search().list(
            part="snippet",
            q=query,
            maxResults=max_results,
            type="playlist"
        )
        return request.execute()

    def search_channels(self, query: str, max_results: int = 5):
        request = self.youtube.search().list(
            part="snippet",
            q=query,
            maxResults=max_results,
            type="channel"
        )
        return request.execute()
