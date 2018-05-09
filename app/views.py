from django.shortcuts import render
from django.views.generic import TemplateView
from django.http.response import JsonResponse
from django.core.cache import cache
from app.api import read_codes, get_all_currencies

class IndexView(TemplateView):
	"""Index view"""
	template_name = 'index.html'

def show_currency(request, from_code:str, to_code:str):
	result = {}
	currencies = __from_cache_or_request()
	for item in currencies[from_code]:
		if item['currency'] == f'{from_code}/{to_code}':
			result = item
			break
	return JsonResponse(result, safe=False)


def show_all_currencies(request):
	currencies = __from_cache_or_request()
	return JsonResponse(currencies, safe=False)

def show_codes(request):
	return JsonResponse(read_codes(), safe=False)

def __from_cache_or_request():
	cache_time = 60*60*36
	currencies = cache.get('currencies')
	if currencies is None or len(currencies) == 0:
		currencies = get_all_currencies()
		cache.set('currencies',currencies, cache_time)
	return currencies