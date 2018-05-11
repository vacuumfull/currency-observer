from django.core.cache import cache

def save_to_cache(currencies: list) -> None:
	"""
	Save currencies to cashe.
	
	currencies - list of currencies
	"""
	cache_time = 60 * 60 * 36
	cache.set('currencies', currencies, cache_time)