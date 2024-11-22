"""This module helps handling aac stream."""
from fastapi import FastAPI
import uvicorn
import requests


app = FastAPI()


@app.get("/start")
def start_streaming():
    """get current track from db"""

    requests.get("stream_ffmpeg:7001/stream", timeout=30)

@app.get("/stop")
def stop_streaming():
    """get current track from db"""

    requests.get("stream_ffmpeg:7001/stop", timeout=30)


if __name__ == "__main__":
    uvicorn.run("main:app", host="main", port=8082, reload=True)
