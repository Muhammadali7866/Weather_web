from django.shortcuts import render
import urllib.request
import json


# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        # print(city)
        api_url = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=612201597d73b0a82b8b13f69a3c09bb').read()
        api_url2 = json.loads(api_url)


        data ={
            "country": city,
            "weather_lon": api_url2['coord']['lon'],
            "weather_description": api_url2['weather'][0]['description'],
            "weather_temperature": int(api_url2['main']['temp']-273),
            "weather_pressure": api_url2['main']['pressure'],
            "weather_humidity": api_url2['main']['humidity'],
            "weather_icon": api_url2['weather'][0]['icon'],
            "weather_wind": api_url2['wind']['speed'],
            "weather_feels" :int(api_url2['main']['feels_like']-273),
            "temp_min" :int(api_url2['main']['temp_min']-273),
            "temp_max" : int(api_url2['main']['temp_max']-273),
            "wind_speed":api_url2['wind']['speed'],
            "wind_deg": api_url2['wind']['deg'],

        }

    else:
        city = None
        data = {
            "country": None,
            "weather_description": None,
            "weather_temperature": None,
            "weather_pressure": None,
            "weather_humidity": None,
            "weather_icon": None,
            "weather_feels": None,
            "temp_min": None,
            "temp_max": None,

        }
    print(data['weather_icon'])
    return render(request, 'index.html', {"city": city, "data": data})

def index2(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        # print(city)
        api_url3 = urllib.request.urlopen('api.openweathermap.org/data/2.5/forecast/daily?q={city name}&cnt={cnt}&appid={API key}').read()
        api_url4 = json.loads(api_url3)


        data1 = {
            "country": city,
            "weather_lon": api_url4['coord']['lon'],
            "weather_descriptions": api_url4['feels_like'][0]['day'],
            #"weather_temperature": int(api_url2['main']['temp']-273),
            #"weather_pressure": api_url2['main']['pressure'],
            #"weather_humidity": api_url2['main']['humidity'],
            #weather_icon": api_url2['weather'][0]['icon'],
            #"weather_wind": api_url2['wind']['speed'],

        }

    else:
        city = None
        data = {
            "country": None,
            "weather_description": None,
            "weather_temperature": None,
            "weather_pressure": None,
            "weather_humidity": None,
            "weather_icon": None,
        }
    print(data['weather_icon'])
    return render(request, 'index.html', {"city": city, "data": data})

