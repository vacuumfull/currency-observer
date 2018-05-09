from django.urls import include, path
from app import views

urlpatterns = ([
	path('codes/', views.show_codes),
	path('currency/all/', views.show_all_currencies),
	path('currency/<str:from_code>/<str:to_code>/', views.show_currency),
])