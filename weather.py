from datetime import datetime
import os
import pytz
import requests
import math
API_KEY = 'ceeb6b096ed1165123d34c3a82d6d159'
API_URL = ('http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&appid={}')
def query_api(city):
    try:
        print(API_URL.format(city, API_KEY))
        data = requests.get(API_URL.format(city, API_KEY)).json()
    except Exception as exc:
        print(exc)
        data = None
    return data