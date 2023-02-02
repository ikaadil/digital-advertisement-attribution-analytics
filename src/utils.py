from flask import request


def get_request_param(param_name):
    request_data = request.get_json()
    param_value = request_data.get(param_name)

    return param_value
