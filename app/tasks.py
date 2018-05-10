from exchanger.celery import app
from app.api import get_all_currencies
from app.helper import save_to_cache

@app.task(name='app.tasks.update_currencies')
def update_currencies():
    currencies = get_all_currencies()
    save_to_cache(currencies)