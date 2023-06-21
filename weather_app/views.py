from django.shortcuts import render
import requests
import datetime
from .config import API_KEY


def index(request):
    if "city" in request.POST:
        city = request.POST["city"]
    else:
        city = "London"


    api_key =  API_KEY
    URL = 'https://api.openweathermap.org/data/2.5/weather'
    PARAMS = {'q':city, 'appid': api_key, 'units': 'metric'}
    r = requests.get(URL, params=PARAMS)
    res=r.json()
    description = res['weather'][0]['description']
    icon = res['weather'][0]['icon']
    temp = res['main']['temp']

    day = datetime.datetime.today()
    

    return render(request, 'weather_app/index.html', {'description': description, 'icon': icon, 'temp': temp, 'day': day, 'city': city})
