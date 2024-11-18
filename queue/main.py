"""This module helps handling aac stream."""
import datetime

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

    last_track = db.get_last_track(database)
    dt = datetime.datetime.now()

    if last_track != None:
        starting_from, length = last_track
        resp = db.add_track(database, track_id, starting_from, length)
    else:
        resp = db.add_track(database, track_id, dt.time(), dt + datetime.timedelta(seconds=30))

    return {"response": resp}


if __name__ == "__main__":
    uvicorn.run("main:app", host="queue", port=8000, reload=True)
