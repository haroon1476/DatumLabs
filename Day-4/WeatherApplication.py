import requests

def get_weather(city):
    api_key = "34f14a79a5e7cc72159d623d01d8181f"  # My API Key
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    # parameters for the API
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  
    }

    # send request
    response = requests.get(base_url, params=params)

    # check status
    if response.status_code == 200:
        data = response.json()
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]

        print(f"\n Weather in {city.capitalize()}:")
        print(f" Temperature: {temperature}°C")
        print(f" Humidity: {humidity}%")
        print(f" Description: {description.capitalize()}")
    else:
        print(" Could not fetch weather data.")


def main():
    city = input("Enter city name: ")
    get_weather(city)

main()
