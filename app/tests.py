from django.test import TestCase
from app.api import get_all_currencies
from app.mocks import success_all
from unittest import mock

class AppTestCase(TestCase):
	
	@mock.patch('app.api.__get_currency', success_all)
	@mock.patch('requests.get', success_all)
	def test__get_all_currencies_success(self):
		print(get_all_currencies())
		assert get_all_currencies() == success_all