from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.db import models
from weather.models import *
from weather.API_Functions import *
b = '0'

menu = [{'title': 'Главная', 'url_n': 'first'},
        {'title': 'Города', 'url_n': 'city_b'}
        ]
def first(request):
    Headline ="⛅Погода⛅"
    BackgroundPainting = True
    b = get_weather('Bryansk')
    w = get_weather_2('Bryansk')
    return render(request, "weather/first.html", context={'menu': menu, 'b' : b,'w':w,'BackgroundPainting':BackgroundPainting,'Headline':Headline})

def city_base(request):
    Headline ="🌤️Погода в разных городах🌤️"
    BackgroundPainting = True
    if request.GET:
        city = request.GET['filed_text']
        vvod = 1
        b = get_weather(city)
        w = get_weather_2(city)
        print(city,b,w)
        BackgroundPainting = True
    else:
        BackgroundPainting = False
        city = '0'
        vvod = 0
        b = 0
        w = ''
    return render(request, "weather/city_base.html", context={'menu': menu, 'b' : b,'w':w,"vvod":vvod,'city':city,'BackgroundPainting':BackgroundPainting,'Headline':Headline})

def week_f(request):
    Headline ="🌦️Погода на неделю🌦️"
    b = get_weather("Bryansk")
    BackgroundPainting = True
    return render(request, "weather/weather for a week.html", context={'b':b,'BackgroundPainting':BackgroundPainting,'Headline':Headline})
def profile_def(request):
    Headline ="Профиль"
    BackgroundPainting = False
    return render(request, "weather/Profile.html", context={'b':b, 'is_login':0,'BackgroundPainting':BackgroundPainting,'Headline':Headline})
def rateOfExchanges_function(request):
    if request.method == 'POST':
        Сurrency1 = request.POST.get('Currencies1')
        Сurrency2 = request.POST.get('Currencies2')
    else:
        Сurrency1 = "RUB"
        Сurrency2 = "USD"
    if request.GET:
        Round = request.GET['Round']
    else:
        Round = 2
    Ruble = GetRateOfExchange(Сurrency1,Сurrency2,Round)
    Headline = "💰💵Курсы валют💵💰"
    BackgroundPainting = False
    return render(request,"weather/rateOfExchanges.html", context={'Ruble':Ruble,'BackgroundPainting':BackgroundPainting,'Headline':Headline,'Сurrency1':Сurrency1,'Сurrency2':Сurrency2})
