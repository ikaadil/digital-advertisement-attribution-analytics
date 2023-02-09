from config import db
from models.Pageview import Pageview
from sqlalchemy.sql import text
from utils import to_dict


def add_pageview_info(pageview: Pageview) -> dict:
    """Every pageview info will be added to database"""

    db.session.add(pageview)
    db.session.commit()
    return {"status": " successfully added"}


def get_pageview_count(date_time):
    """Every pageview will be counted group by different domain.
    Where null domain means direct visit.
    """

    query = f"""
    SELECT referrer_domain,
       Count(*)
    FROM   pageviews
    WHERE  created_at >= "{date_time}"
        AND user_id IS NULL
    GROUP  BY referrer_domain 
    """
    result = db.session.execute(text(query)).fetchall()
    return to_dict(result)


def get_succeeded_ad(date_time):
    """If a user visit a page from advertisement and signup in the app, 
    then his fingerprint will be same. So if we find any fingerprint in
    events table, we consider this as successful advertisement. Where null 
    domain means direct visit"""

    query = f"""
    SELECT referrer_domain,
    Count(DISTINCT( fingerprint ))
    FROM   pageviews
    WHERE  created_at >= "{date_time}"
        AND user_id IS NULL
        AND fingerprint IN (SELECT fingerprint
                            FROM   events
                            WHERE  NAME = "signup")
    GROUP  BY referrer_domain 
    """
    result = db.session.execute(text(query)).fetchall()
    return to_dict(result)


def get_analysis(date_time: str, show_succeeded_ad: bool) -> dict:
    """Here we generate pageview count from advertisement and
    succeeded advertisement count group by different domain. If 
    input data_time is null, we consider default date as '1900-01-01'
    """

    if not date_time:
        date_time = '1900-01-01'
    response = {}
    response["pageview_count"] = get_pageview_count(date_time)
    if show_succeeded_ad:
        response["succeeded_ad_count"] = get_succeeded_ad(date_time)
    return response
