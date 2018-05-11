from exchanger.celery import app
from app.api import Api
from app.helper import save_to_cache

api = Api()

@app.task(name='app.tasks.update_currencies')
def update_currencies():
	"""Update currencies task"""
	currencies = api.get_all_currencies()
	save_to_cache(currencies)