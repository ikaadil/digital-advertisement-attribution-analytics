from utils import get_arg_param, get_request_param, to_json
from models.Event import Event, db
import datetime
from sqlalchemy.sql import text


def add():
    name = get_request_param("name")
    fingerprint = get_request_param("fingerprint")
    user_id = get_request_param("user_id")
    created_at = get_request_param("created_at")
    created_at = datetime.datetime.strptime(created_at, '%Y-%m-%d %H:%M:%S.%f')
    event = Event(name=name, fingerprint=fingerprint,
                  user_id=user_id, created_at=created_at)
    db.session.add(event)
    db.session.commit()

    return {"status": " successfully added"}


def get():
    # TODO: Implement query to count distinct user_id group by interval
    date_time = get_arg_param("date_time")
    query = f'select count(distinct(user_id)) from events where created_at>="{date_time}"'
    response = db.session.execute(text(query)).fetchall()

    return to_json(response)
