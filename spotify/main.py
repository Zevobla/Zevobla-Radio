"""This module helps handling spotify streaming data."""
from stream_spotify import StreamFromSpotify
from config import Config

import uvicorn
from fastapi import FastAPI


conf = Config()
app = FastAPI()
spotify = StreamFromSpotify(
    conf.conf["client_id"],
    conf.conf["client_secret"]
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
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)