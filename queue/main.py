"""This module helps handling aac stream."""
import datetime

from fastapi import FastAPI
import uvicorn

import db


app = FastAPI()


@app.get("/current")
def get_current_track():
    """get current track from db"""

    with db.SessionLocal() as session:
        return {"response": db.get_last_track(session)}


@app.post("/track/{track_id}")
def add_track(track_id: str):
    """add track to the db"""

    with db.SessionLocal() as session:
        last_track = db.get_last_track(session)
        dt = datetime.datetime.now()

        if last_track != None:
            starting_from, length = last_track
            resp = db.add_track(session, track_id, starting_from, length)
        else:
            resp = db.add_track(session, track_id, dt + datetime.timedelta(seconds=30), datetime.time(minute=5))

    return {"response": resp}


if __name__ == "__main__":
    uvicorn.run("main:app", host="queue", port=7002, reload=True)
