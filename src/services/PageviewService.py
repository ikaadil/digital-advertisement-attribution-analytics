from config import db
from models.Pageview import Pageview
from sqlalchemy.sql import text
from utils import to_dict


def add_pageview_info(pageview: Pageview) -> dict:
    db.session.add(pageview)
    db.session.commit()
    return {"status": " successfully added"}


def get_pageview_count(date_time):
    query = f'select referrer_domain, count(*) from pageviews where created_at>="{date_time}" group by referrer_domain'
    result = db.session.execute(text(query)).fetchall()
    return to_dict(result)


def get_succeeded_ad(date_time):
    query = f'select referrer_domain, count(distinct(fingerprint)) from pageviews where created_at>="{date_time}" and fingerprint IN (select fingerprint from events where name="signup") group by referrer_domain'
    result = db.session.execute(text(query)).fetchall()
    return to_dict(result)


def get_analysis(date_time: str, show_succeeded_ad: bool) -> dict:
    if not date_time:
        date_time = '1900-01-01'
    response = {}
    response["pageview_count"] = get_pageview_count(date_time)
    if show_succeeded_ad:
        response["succeeded_ad_count"] = get_succeeded_ad(date_time)
    return response
