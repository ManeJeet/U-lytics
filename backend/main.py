from fastapi import FastAPI
from app.api.routers import search, videos, playlists, channels

app = FastAPI(title="YouTube Data API App")

app.include_router(search.router, prefix="/search", tags=["Search"])
app.include_router(videos.router, prefix="/videos", tags=["Videos"])
app.include_router(playlists.router, prefix="/playlists", tags=["Playlists"])
app.include_router(channels.router, prefix="/channels", tags=["Channels"])
