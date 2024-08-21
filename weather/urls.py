# weather/urls.py
from django.urls import path
from .views import WeatherView, we

urlpatterns = [
    # path('', home, name='home'), 
    path('<str:city>/', WeatherView.as_view(), name='weather'),
    path('', we, name='we'),
]
