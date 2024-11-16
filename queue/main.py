"""This module helps handling aac stream."""
import os

from fastapi import FastAPI
import uvicorn

import db


app = FastAPI()
database = db.get_db()


@app.get("/current")
def get_current_track():
    """get current track from db"""

    return {"response": db.get_last_track(database)}


@app.post("/track/{track_id}")
def add_track(track_id: str):
    """add track to the db"""

    starting_from, length = db.get_last_track(database)

    return {"response": db.add_track(database, track_id, starting_from, length)}


if __name__ == "__main__":
    uvicorn.run("main:app", host="queue", port=8000, reload=True)
