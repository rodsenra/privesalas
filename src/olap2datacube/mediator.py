# coding: utf-8
__author__ = 'rodsenra'

from flask import Flask, Response, request
from olap2datacube.util import validate_json


app = Flask(__name__)

@app.route("/generateDimInstances", methods=['POST'])
def generateDimInstances():
    if request.method == 'POST':
        validation_error = validate_json(request)
        if validation_error is not None:
            return validation_error

        return Response(status=200)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)