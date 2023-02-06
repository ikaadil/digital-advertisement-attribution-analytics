from flask import request
import datetime
from tldextract import tldextract


def get_request_param(param_name):
    request_data = request.get_json()
    param_value = request_data.get(param_name)
    return param_value


def get_arg_param(param_name):
    return request.args.get(param_name)


def to_datetime(_datetime):
    return datetime.datetime.strptime(_datetime, '%Y-%m-%d %H:%M:%S.%f')


def extract_domain(url):
    if not url:
        return None
    return tldextract.extract(url).domain


def to_dict(data):
    result = []
    for i in data:
        result.append({i[0]: i[1]})
    return result
