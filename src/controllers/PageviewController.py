from sqlalchemy.sql import text

from utils import get_request_param, get_arg_param, to_datetime, extract_domain, to_json
from models.Pageview import Pageview
from config import db


def add():
    fingerprint = get_request_param("fingerprint")
    user_id = get_request_param("user_id")
    url = get_request_param("url")
    referrer_url = get_request_param("referrer_url")
    referrer_domain = extract_domain(referrer_url)
    created_at = get_request_param("created_at")
    created_at = to_datetime(created_at)
    pageview = Pageview(fingerprint=fingerprint, user_id=user_id,
                        url=url, referrer_url=referrer_url, referrer_domain=referrer_domain, created_at=created_at)
    db.session.add(pageview)
    db.session.commit()

    return {"status": " successfully added"}


def get():
    # TODO: Add a different table for domain
    # TODO: Take ad site as variable from request
    # TODO: Implement result based on intervals

    date_time = get_arg_param("date_time")
    query = f'select referrer_domain, count(*) from pageviews where created_at>="{date_time}" group by referrer_domain'
    response = db.session.execute(text(query)).fetchall()
    return to_json(response)
