# coding: utf-8
import json
from flask_testing import TestCase
from olap2datacube.catalogue import app

__author__ = 'rodsenra'


class TestCatalogue(TestCase):

    def create_app(self):
        return app

    def test_valid_queryExecutorRDB(self):
        input_data = open("examples/request_catalogue_queryExecutorRDB.sql").read()
        response = self.client.post(
                    "/queryExecutorRDB",
                    content_type="application/x-sql",
                    data=input_data)
        self.assert200(response)

    def test_invalid_queryExecutorRDB_no_payload(self):
        response = self.client.post(
                    "/queryExecutorRDB",
                    content_type="application/x-sql")
        self.assert400(response)

    def test_valid_getModelRDB(self):
        json_output_data = json.load(open("examples/response_catalogue_getModelRDB.json"))
        response = self.client.post(
                    "/getModelRDB",
                    headers=[('Accept', 'application/json')],
                    content_type="application/x-sql",
                    data="Select * from Table X")
        self.assert200(response)
        self.assertEqual(response.json, json_output_data)

    def test_invalid_getModelRDB_no_accept_header(self):
        response = self.client.post(
                    "/getModelRDB",
                    content_type="application/x-sql",
                    data="Select * from Table X")
        self.assert400(response)
