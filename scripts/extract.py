import requests
import json
import  logging
import pandas as pd
import time




logging.basicConfig(level=logging.INFO,
                    filename='../logs/weather.log',
                    format='%(asctime)s %(levelname)s %(message)s')


def fetch_data(city_name):
    API_KEY = "b70f5725f31f24110d46282a364a6878"
    logging.info(f"Extracting data from started")
    all_data=[]
    try:
        for city in city_name:
            time.sleep(2)
            URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            response = requests.get(URL)
            time.sleep(1)
            logging.info(f"Checking response status code from :{URL}")

            if response.status_code == 200:
                json_data = response.json()
                logging.info(f"Response status are :{response.status_code}")
                try:
                    logging.info(f" Start Saving Raw data In data file for backup")
                    with open("../data/raw_weather.json", "a") as file:
                        file.write(json.dumps(json_data) + "\n")
                        logging.info(f"Data  Successfully saved in data file for backup")
                        all_data.append(json_data)
                except Exception as e:
                    logging.error(f"Failed to Save Raw Data:{e}")


    except requests.exceptions.HTTPError as e:
        logging.error(f"HTTP Error: {e}")
    except requests.exceptions.RequestException as e:
        logging.error(f"General API error{e}")

    logging.info(f"Extracting data from :{URL} completed")

    return all_data

