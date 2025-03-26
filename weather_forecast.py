import requests
import json

def weather_data(city,api_key):
    queries = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    base_url = f"http://api.openweathermap.org/data/2.5/weather"

    try:
        response = requests.get(base_url, params=queries)
        response.raise_for_status()
    except Exception as e:
        print("An error occured: ", e)

    if response.status_code != 200:
        print(response.json()['message'])
        return
    
    weather_data = response.json()
    with open('weather_data.json', 'w') as f:
        json.dump(weather_data, f, indent=4)
    temperature = weather_data['main']['temp']
    print(f"Temperature in {city} : {temperature} °C")


def main():
    api_key = "c9c94ffba0a82bf92411cc8fce297e00"
    city = input("Enter the city name: ")
    weather_data(city,api_key)

if __name__ == "__main__":
    main()