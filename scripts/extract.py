import requests
import json


city_name=input("Enter the city name:")
API_KEY="b70f5725f31f24110d46282a364a6878"
URL=f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"

def fetch_data():
    try:
        response = requests.get(URL)
        if response.status_code == 200:
            json_data = response.json()
        data = json.dumps(json_data, indent=4)
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
    except requests.exceptions.RequestException as e:
        print(f"General API error{e}")

    return data

