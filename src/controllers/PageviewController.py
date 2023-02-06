from sqlalchemy.sql import text

from utils import get_request_param, get_arg_param, to_datetime, extract_domain, to_dict
from models.Pageview import Pageview
import json
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
    # TODO: Add a service for the different condition
    response = {}
    date_time = get_arg_param("date_time")
    show_succeeded_ad = get_arg_param("show_succeeded_ad")
    query = f'select referrer_domain, count(*) from pageviews where created_at>="{date_time}" group by referrer_domain'
    result = db.session.execute(text(query)).fetchall()
    response["pageview_count"] = to_dict(result)
    if show_succeeded_ad:
        query = f'select referrer_domain, count(distinct(fingerprint)) from pageviews where created_at>="{date_time}" and fingerprint IN (select fingerprint from events) group by referrer_domain'
        result = db.session.execute(text(query)).fetchall()
        response["succeeded_ad_count"] = to_dict(result)
    return json.dumps(response)
