# coding: utf-8

__author__ = 'rodsenra'

from flask_testing import TestCase


def TestMediator(TestCase):

    def create_app(self):
        app = Flask(__name__)
        return app

    def test_request_generateDimInstances(self):
        input_data = open("examples/request_mediator_generateDimInstances.json").read()
        response = self.client.post(
                    "/generateDimInstances",
                    content_type="application/json",
                    data=input_data)
        self.assertEquals(response.status_code, 200)
