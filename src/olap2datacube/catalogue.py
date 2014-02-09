# coding: utf-8

__author__ = 'rodsenra'

import json
from flask import Flask, Response, request, jsonify
from olap2datacube.util import validate_sql, error

app = Flask(__name__)

@app.route("/queryExecutorRDB", methods=['POST'])
def queryExecutorRDB():
    if request.method == 'POST':
        error = validate_sql(request)
        if error is not None:
            return error

        return Response(status=200)

@app.route("/getModelRDB", methods=['POST'])
def getModelRDB():
    if request.method == 'POST':
        validation_error = validate_sql(request)
        if validation_error is not None:
            return validation_error

        # Test if client accepts the response content-type: application/json
        if 'Accept' not in request.headers.keys():
            return error(400, "Client must accept content-type application/json")

        if 'application/json' not in request.headers['ACCEPT']:
            return error(400, "Client must accept content-type application/json in addition to {0}".format(request.headers['Accept']))

        # FIXME: returning mocked results
        mocked_response = json.load(open('examples/response_catalogue_getModelRDB.json'))
        return jsonify(mocked_response)

@app.route("/generateTriples", methods=['GET'])
def generateTriples():
    if request.method == 'GET':
        model_id = request.args.get('model_id', None)
        if model_id is None:
            return error(400, "Parameter model_id must is mandatory")

        # TODO: generate Triples here

        return Response(status=200)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)