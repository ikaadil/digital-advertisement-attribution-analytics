from utils import get_request_param
from models.Event import Event
from models.Event import db
import datetime


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
