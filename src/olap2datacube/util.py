# coding: utf-8

__author__ = 'rodsenra'

from flask import jsonify


class BadRequest(Exception):
    pass


def error(status_code, message, extra_dict=None):
    error_response = {"message": message}
    if extra_dict is not None:
        error_response.update(extra_dict)
    response = jsonify(error_response)
    response.status_code = status_code
    return response


def validate_json(request):
    if not request.content_type.startswith("application/json"):
        return error(400, "Content-type must be application/json instead of {0}".format(request.content_type))
    try:
        request.json
        if not request.json:
            raise BadRequest()
    except BadRequest:
        return error(400, "required parameter missing", {"parameter": {"file": request.data}})


def validate_sql(request):
    if not request.content_type.startswith("application/x-sql"):
        return error(400, "Content-type must be application/x-sql instead of {0}".format(request.content_type))
    try:
        # TODO: validate SQL in here
        if not request.data:
            raise BadRequest()
    except BadRequest:
        return error(400, "required parameter missing", {"parameter": {"file": request.data}})
