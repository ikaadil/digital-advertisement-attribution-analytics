from flask import request
import datetime


def get_request_param(param_name):
    request_data = request.get_json()
    param_value = request_data.get(param_name)

    return param_value


def get_arg_param(param_name):
    return request.args.get(param_name)


def to_datetime(_datetime):
    return datetime.datetime.strptime(_datetime, '%Y-%m-%d %H:%M:%S.%f')
