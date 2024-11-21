"""This module helps handling aac stream."""
from subprocess import Popen
import os

from fastapi import FastAPI
import uvicorn

import stream


def handle_config() -> dict[str, dict[str, str]]:
    """This functions helps unpack config"""

    conf = {}

    for var in os.environ:
        if var[:3] == "ROUT":
            g = var.split("_")
            conf[g[1]][g[2]] = g[3]

    return conf


app = FastAPI()
streams_sessions: list[Popen] = []
config = handle_config()


@app.get("/stream")
def stream_to():
    """Starts streaming"""

    for param in config.values():
        process = stream.Stream(
            codec=param["codec"],
            otype=param["type"],
            path=param["path"]
        )

        streams_sessions.append(
            process
        )

        process.start()

    return True


@app.get("/stop")
def stream_stop():
    """Starts streaming"""

    for service in streams_sessions:
        service.stop()

    return True


if __name__ == "__main__":
    uvicorn.run("main:app", host="stream_ffmpeg", port=8081, reload=True)
    stream_to()
