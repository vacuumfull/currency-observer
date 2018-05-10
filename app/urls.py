from django.urls import include, path
from app.api import Api

api = Api()

urlpatterns = ([
	path('codes/', api.show_codes),
	path('currency/all/', api.show_all_currencies),
	path('currency/<str:from_code>/<str:to_code>/', api.show_currency),
])