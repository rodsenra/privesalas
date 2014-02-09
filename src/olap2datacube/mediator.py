# coding: utf-8
__author__ = 'rodsenra'

from flask import Flask, jsonify, Response, request


class BadRequest(Exception):
    pass

app = Flask(__name__)


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
        if request.json is None:
            raise BadRequest()
    except BadRequest:
        return error(400, "required parameter missing", {"parameter": {"file": request.data}})


@app.route("/generateDimInstances", methods=['POST'])
def generateDimInstances():
    if request.method == 'POST':
        validate_json(request)
        return Response(status=200)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)