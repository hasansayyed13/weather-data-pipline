import json
import pandas as pd
from extract import fetch_data
from datetime import datetime


def tranform_data():
    data = fetch_data()
    d=json.loads(data)


    city=d['name']
    longitude=d['coord']['lon']
    latitude=d['coord']['lat']
    temperature=d['main']['temp']
    min_temp=d['main']['temp_min']
    max_temp=d['main']['temp_max']
    humidity=d['main']['humidity']
    pressure=d['main']['pressure']
    wind_speed=d['wind']['speed']
    weather_description=d['weather'][0]['main']
    date=datetime.now()


    print(f"City:{city}")
    print(f'longitude:{longitude}')
    print(f'latitude:{latitude}')
    print(f'temperature:{temperature}')
    print(f'min_temp:{min_temp}')
    print(f'max_temp:{max_temp}')
    print(f'humidity:{humidity}')
    print(f'pressure:{pressure}')
    print(f'wind_speed:{wind_speed}')
    print(f'weather_description:{weather_description}')
    print(f'date:{date}')




    return (city,longitude,latitude,temperature,min_temp,max_temp,humidity,
            pressure,wind_speed,weather_description,date)

