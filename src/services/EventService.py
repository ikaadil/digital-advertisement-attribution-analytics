from sqlalchemy.sql import text
from config import db
from models.Event import Event


def add_event(event: Event):
    """A new event will be added to database"""

    db.session.add(event)
    db.session.commit()
    return {"status": " successfully added"}


def get_user_count(date_time: str):
    """Distinct user count will be fetched from given date time. 
    If the date time is not provided then considered default 
    date as '1900-01-01'
    """

    if not date_time:
        date_time = '1900-01-01'
    query = f"""
    SELECT Count(DISTINCT( user_id ))
    FROM   events
    WHERE  NAME = "signup"
    AND created_at >= "{date_time}" 
    """
    response = db.session.execute(text(query)).fetchone()
    return {'number_of_unique_user': str(response[0])}
