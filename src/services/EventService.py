from sqlalchemy.sql import text
from config import db
from models.Event import Event


def add_event(event: Event):
    db.session.add(event)
    db.session.commit()
    return {"status": " successfully added"}


def get_user_count(date_time: str):
    if not date_time:
        date_time = '1900-01-01'
    query = f'select count(distinct(user_id)) from events where created_at>="{date_time}"'
    response = db.session.execute(text(query)).fetchone()
    return {'number_of_unique_user': str(response[0])}
