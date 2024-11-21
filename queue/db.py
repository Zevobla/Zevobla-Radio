"""This module represent Track model and Interface for db"""
import datetime
import os

from sqlalchemy import create_engine, Column, Integer, String, DateTime, Time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session


c = os.environ
Base = declarative_base()
engine = create_engine(c["DB_URL"], echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Track(Base):
    """This class represent each track that which be played"""
    __tablename__ = "tracks"

    id = Column(Integer, primary_key=True, index=True)
    track_id = Column(String)
    starting_from = Column(DateTime)
    length = Column(Time)

def init_db():
    """Initialize the database and create tables."""
    Base.metadata.create_all(bind=engine)

def get_last_track(session: Session):
    """Retrieve the id of the last track in the database."""
    last_track = session.query(Track).order_by(Track.id.desc()).first()
    return last_track.track_id if last_track else None
    
def add_track(db: Session, track_id: str, starting_from: datetime.datetime, length: datetime.time):
    """
    Adds a new track to the database.

    Args:
        db (Session): The database session.
        track_id (str): The ID of the track.
        starting_from (datetime.datetime): The starting time of the track.
        length (datetime.time): The length of the track.
    """
    try:
        db.add(
            Track(
                track_id=track_id, 
                starting_from=starting_from, 
                length=length
            )
        )
        db.commit()
        return True
    except Exception as e:
        print(f"Error adding track: {e}")
        db.rollback()
        return False

def void(db: Session) -> tuple[str]:
    """
    Gets the starting_from and length parameters from the last track in the database.

    Args:
        db (Session): The database session.

    Returns:
        datetime.datetime: The starting_from parameter of the last track, or None if there are no tracks.
        datetime.time: The length parameter of the last track, or None if there are no tracks.
    """
    try:
        last_track = db.query(Track).order_by(Track.starting_from.desc()).first()
        if last_track:
            return last_track.starting_from, last_track.length
        else:
            return None
    except Exception as e:
        print(f"Error getting last track starting_from: {e}")
        return None
