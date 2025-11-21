import json
import pandas as pd
from extract import fetch_data
from datetime import datetime
import json
import os
import logging

logging.basicConfig(level=logging.INFO,
                    filename="../data/weather.log",
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def tranform_data(data):
    logging.info("Start Transform Data")
    weather_data=[]

    try:
        for city_data in data:
            logging.info(" Start Transform Data")
            city = city_data.get('name', "unknown")
            longitude = city_data.get('coord', {}).get("lon", 0)
            latitude = city_data.get('coord', {}).get("lat", 0)
            temperature = city_data.get("main", {}).get("temp", 0)
            min_temp = city_data.get("main", {}).get("temp_min", 0)
            max_temp = city_data.get("main", {}).get("temp_max", 0)
            humidity = city_data.get("main", {}).get("humidity", 0)
            pressure = city_data.get("main", {}).get("pressure", 0)
            wind_speed = city_data.get("wind", {}).get("speed", 0)
            weather_description = city_data.get("weather", [{}])[0].get("main", "No Description")
            country = city_data.get("sys", {}).get('country', "unknown")
            date = datetime.now()

            record = {
                "city": city,
                "longitude": longitude,
                "latitude": latitude,
                "temperature": temperature,
                "min_temp": min_temp,
                "max_temp": max_temp,
                "humidity": humidity,
                "pressure": pressure,
                "wind_speed": wind_speed,
                "weather_description": weather_description,
                "Country": country,
                "date": date
            }
            weather_data.append(record)

        df=pd.DataFrame(weather_data)
        file_path=os.path.isfile("../data/clean_weather.csv")
        df.to_csv("../data/clean_weather.csv",mode='a',index=False,header=not file_path)



    except Exception as e:
        logging.error(f"Failed to Transform Data:{e}")

    return df

