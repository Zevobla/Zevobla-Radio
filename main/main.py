"""This module helps handling aac stream."""
import datetime

from fastapi import FastAPI
import uvicorn
import requests


app = FastAPI()


@app.get("/start")
def start_streaming():
    """get current track from db"""

    r = requests.get("stream_ffmpeg:7001/stream")

@app.get("/stop")
def stop_streaming():
    """get current track from db"""

    r = requests.get("stream_ffmpeg:7001/stop")


if __name__ == "__main__":
    uvicorn.run("main:app", host="main", port=8082, reload=True)
