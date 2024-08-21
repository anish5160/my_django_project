# weather/views.py
import requests
from django.http import JsonResponse
from django.views import View



# weather/views.py

from django.http import HttpResponse

# def home(request):
#     return HttpResponse(" Please use the format /weather to run the city query parameter..")

def we(request):
    return HttpResponse("Welcome to the Weather App! Format /cityname to get weather info of any city you want.")
class WeatherView(View):
    def get(self, request, city):
        
        
        if not city:
            return JsonResponse({'error': 'Enter the city'}, status=400)

        api_key = '895063bfc2df94b5e6b9fa0c745fa3fe'  # Replace with your API key
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            weather_data = response.json()

            return JsonResponse({
                'city': weather_data['name'],
                'temperature': weather_data['main']['temp'],
                'description': weather_data['weather'][0]['description'],
            })

        except requests.exceptions.HTTPError as http_err:
            return JsonResponse({'error': f'HTTP error occurred: {http_err}'}, status=500)
        except requests.exceptions.RequestException as err:
            return JsonResponse({'error': f'Error occurred: {err}'}, status=500)
