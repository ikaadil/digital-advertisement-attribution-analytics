
from utils import get_request_param, get_arg_param, to_datetime, extract_domain
from models.Pageview import Pageview
from services.PageviewService import add_pageview_info, get_analysis
import json


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
    return add_pageview_info(pageview)


def get():
    # TODO: Add a different table for domain
    # TODO: Take ad site as variable from request
    # TODO: Implement result based on intervals
    date_time = get_arg_param("date_time")
    show_succeeded_ad = get_arg_param("show_succeeded_ad")
    response = get_analysis(date_time, show_succeeded_ad)
    return json.dumps(response)
