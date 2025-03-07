from django.urls import path
from weather.views import *
from weather import views
urlpatterns = [
    path('',first,name = 'first'),
    path('city_base',city_base,name = 'city_b'),
    path('weather for a week',week_f,name = 'week'),
    path('profile',profile_def,name = 'profile_name'),
    path('rateOfExchanges',rateOfExchanges_function,name = 'rateOfExchanges_name'),
]
