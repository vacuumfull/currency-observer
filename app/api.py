from django.conf import settings
from requests.exceptions import RequestException
from django.conf import settings
import requests
import json

API_URL = 'https://currencydatafeed.com/api/data.php'
MAIN_CURRENCIES = ('EUR', 'USD', 'CSK', 'PLN')

def __get_currency(currency: str):
	try:
		response = requests.get(f'{API_URL}?token={settings.CURRENCY_TOKEN}&currency={currency}')
		return response.json()
	except RequestException as re:
		return {'error': f'RequestException: {re}'}
	except ValueError as ve:
		return {'error': f'JsonException: {ve}'}

def read_codes():
	"""Read currency codes from json"""
	codes_file = open(f'{settings.BASE_DIR}/resources/fixtures/codes.json')
	codes = json.load(codes_file)
	codes_file.close()
	return codes

def get_all_currencies():
	"""Get currencies for all main codes"""
	currencies = {}
	codes = read_codes()
	for currency in MAIN_CURRENCIES:
		currency_param = ''
		for code in codes:
			if currency != code["code"]:
				currency_param += f'{currency}/{code["code"]}+'
		result = __get_currency(currency_param[0:-1])
		print(result)
		if 'error' not in result:
			currencies[currency] = result['currency']
	return currencies