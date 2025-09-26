import pandas as pd
import numpy as np
import requests
import json
import mysql.connector as mysql
from datetime import datetime


def mysqlconnection():
    try:
        db = mysql.connect(
            host="localhost",
            user="root",
            passwd="1234",
            database="weatherdata")
        print("CONNECTION SUCCESS")
        cursor = db.cursor()
        create_query = """
                        CREATE TABLE IF NOT EXISTS weather(
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        name VARCHAR(50),
                        temp FLOAT,
                        humidity INT,
                        description VARCHAR(60),
                        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                    )
                """

        cursor.execute(create_query)
        return db
    except ValueError as e:
        print(e)




def fetchweather():
    API_KEY="b70f5725f31f24110d46282a364a6878"
    city_name=input("Enter the city name:")
    API_URL=f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"
    response = requests.get(API_URL)
    json_data = response.json()
    data=json.dumps(json_data,indent=4)
    name = json_data['name']
    temp = json_data['main']['temp']
    humidity = json_data['main']['humidity']
    description = json_data['weather'][0]['description']

    print(f"Name: {name}\n"
          f"Temperature: {temp}\n"
          f"Humidity: {humidity}\n"
          f"Description: {description}\n")

    return name, temp, humidity, description



def insert_weather_data():
    db=mysqlconnection()
    cursor = db.cursor()


    name, temp, humidity, description=fetchweather()

    insert_query=""" INSERT INTO weather(name,temp,humidity,description,timestamp)VALUES(%s,%s,%s,%s,%s)"""

    values=(name,temp,humidity,description,datetime.now())
    cursor.execute(insert_query,values)
    db.commit()
    print("Data inserted")
    cursor.close()
    db.close()


insert_weather_data()