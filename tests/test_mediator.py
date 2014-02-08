# coding: utf-8
from flask_testing import TestCase
from flask import Flask
from olap2datacube.mediator import app

__author__ = 'rodsenra'


class TestMediator(TestCase):

    def create_app(self):
        return app

    def test_request_generateDimInstances(self):
        input_data = open("examples/request_mediator_generateDimInstances.json").read()
        response = self.client.post(
                    "/generateDimInstances",
                    content_type="application/json",
                    data=input_data)
        self.assert200(response)
