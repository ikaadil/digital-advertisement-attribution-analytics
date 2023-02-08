from utils import get_arg_param, get_request_param, to_datetime
from models.Event import Event
from services.EventService import add_event, get_user_count


def add():
    name = get_request_param("name")
    fingerprint = get_request_param("fingerprint")
    user_id = get_request_param("user_id")
    created_at = get_request_param("created_at")
    created_at = to_datetime(created_at)
    event = Event(name=name, fingerprint=fingerprint,
                  user_id=user_id, created_at=created_at)
    return add_event(event)


def get():
    # TODO: Implement query to count distinct user_id group by interval
    date_time = get_arg_param("date_time")
    return get_user_count(date_time)
