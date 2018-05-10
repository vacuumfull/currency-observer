from django.test import TestCase
from app.api import Api
from app.mocks import success_one, success_all, success_err
from unittest import mock
import requests


def mocked_requests_get_one(*args, **kwargs):
	class MockResponse:

		def __init__(self, json_data):
			self.json_data = json_data

		def json(self):
			return self.json_data

	return MockResponse(success_one)


class AppTestCase(TestCase):
	
	def setUp(self):
		self.api = Api()

	@mock.patch('requests.get', side_effect=mocked_requests_get_one)
	def test__get_currency(self, mockget):
		curr = 'PLN/AED'
		json_data = self.api.get_currency(curr)

		assert json_data == success_one
	

	@mock.patch('requests.get', side_effect=ValueError)
	def test__get_currency_err(self, mockget):
		curr = 'PLN/AED'
		json_data = self.api.get_currency(curr)

		assert json_data == success_err

	@mock.patch('app.api.Api.get_currency',return_value=success_all)
	def test__get_all_currencies(self, mockget):
		result = self.api.get_all_currencies()
		assert result['EUR'] == success_all['currency']

	
	def test__get_codes(self):
		assert len(self.api.read_codes()) == 51