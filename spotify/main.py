"""This module helps handling spotify streaming data."""
import os

import uvicorn
from fastapi import FastAPI

from stream_spotify import StreamFromSpotify


app = FastAPI()
spotify = StreamFromSpotify(
    os.environ["SPOTIPY_CLIENT_ID"],
    os.environ["SPOTIPY_CLIENT_SECRET"]
)


@app.get("/playlist/{playlist_id}")
def get_playlist(playlist_id: str):
    """Handle trck ids of playlist"""

    return {"response": spotify.get_playlist(playlist_id)}


@app.get("/stream/{track_id}")
def get_track(track_id: str):
    """Handle track's stream"""

    return {"response": spotify.stream_track(track_id)}


if __name__ == "__main__":
    uvicorn.run("main:app", host="spotify", port=8000, reload=True)
