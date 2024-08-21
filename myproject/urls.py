# myproject/urls.py
from django.contrib import admin
from django.urls import path, include
# from weather.views import home, we

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', home, name='home'), 
    # path('cityname/', ),
    path('weather/', include('weather.urls')),
]
