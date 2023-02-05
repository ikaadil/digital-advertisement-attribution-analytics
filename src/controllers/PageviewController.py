from utils import get_arg_param, get_request_param, to_datetime
from models.Pageview import Pageview
from config import db


def add():
    fingerprint = get_request_param("fingerprint")
    user_id = get_request_param("user_id")
    url = get_arg_param("url")
    referrer_url = get_arg_param("referrer_url")
    created_at = get_request_param("created_at")
    created_at = to_datetime(created_at)
    pageview = Pageview(fingerprint=fingerprint, user_id=user_id,
                        url=url, referrer_url=referrer_url, created_at=created_at)
    db.session.add(pageview)
    db.session.commit()

    return {"status": " successfully added"}
