from django.shortcuts import render
from app.helper import save_to_cache
from django.http.response import JsonResponse
from django.conf import settings
from requests.exceptions import RequestException
from django.conf import settings
from django.core.cache import cache
import requests
import json


class Api():

	def __init__(self):
		self.API_URL = 'https://currencydatafeed.com/api/data.php'
		self.MAIN_CURRENCIES = ('EUR', 'USD', 'CSK', 'PLN')

	def get_currency(self, currency: str):
		"""Get currencies.
		
		currency -- string in format 'EUR/USD'
		"""
		try:
			response = requests.get(f'{self.API_URL}?token={settings.CURRENCY_TOKEN}&currency={currency}')
			return response.json()
		except RequestException as re:
			return {'error': f'RequestException: {re}'}
		except ValueError as ve:
			return {'error': f'JsonException: {ve}'}
	
	@staticmethod
	def read_codes():
		"""Read currency codes from json"""
		codes_file = open(f'{settings.BASE_DIR}/resources/fixtures/codes.json')
		codes = json.load(codes_file)
		codes_file.close()
		return codes

	def get_all_currencies(self):
		"""Get currencies for all main codes"""
		currencies = {}
		codes = self.read_codes()
		for currency in self.MAIN_CURRENCIES:
			currency_param = ''
			for code in codes:
				if currency != code["code"]:
					currency_param += f'{currency}/{code["code"]}+'
			result = self.get_currency(currency_param[0:-1])
			if 'error' not in result:
				currencies[currency] = result['currency']
			else:
				currencies[currency] = result
		return currencies

	
	def show_currency(self, request, from_code:str, to_code:str):
		result = {}
		currencies = self.__from_cache_or_request()
		for item in currencies[from_code]:
			if item['currency'] == f'{from_code}/{to_code}':
				result = item
				break
		return JsonResponse(result, safe=False)


	def show_all_currencies(self, request):
		"""
		Show all currencies in json.

		request -- request object
		"""
		currencies = self.__from_cache_or_request()
		return JsonResponse(currencies, safe=False)

	def show_codes(self, request):
		"""
		Show countries and codes and currencies in json"""
		return JsonResponse(self.read_codes(), safe=False)

	def __from_cache_or_request(self):
		"""Get currencies fron cache or make request"""
		currencies = cache.get('currencies')
		if currencies is None or len(currencies) == 0:
			currencies = self.get_all_currencies()
			save_to_cache(currencies)
		return currencies