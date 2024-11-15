"""This module helps handling aac stream."""
from subprocess import Popen

from fastapi import FastAPI
import uvicorn

import stream
from config.config import Config


app = FastAPI()
streams_sessions: list[Popen] = []


@app.get("/stream")
def stream_to():
    """Starts streaming"""

    c = Config().conf["out"]

    for service in c.keys():
        streams_sessions.append(
            stream.Stream(
                codec=c[service]["codec"],
                otype=c[service]["type"],
                path=c[service]["path"]
            )
        )

    return True


@app.get("/stop")
def stream_stop():
    """Starts streaming"""

    for service in streams_sessions:
        service.kill()

    return True


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8081, reload=True)
