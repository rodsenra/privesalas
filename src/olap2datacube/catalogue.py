# coding: utf-8

__author__ = 'rodsenra'

from flask import Flask, Response, request
from olap2datacube.util import validate_sql

app = Flask(__name__)

@app.route("/queryExecutorRDB", methods=['POST'])
def queryExecutorRDB():
    if request.method == 'POST':
        error = validate_sql(request)
        if error is not None:
            return error

        return Response(status=200)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)