import requests


def fetch_coordinates(api_key, city):
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={api_key}"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        if data:
            for result in data:
                latitude = result['lat']
                longitude = result['lon']
                print(f"City: {city}")
                print(f"Latitude: {latitude}")
                print(f"Longitude: {longitude}")
                print("-------------------------")
                fetch_weather(api_key, latitude,longitude)
        else:
            print("No matching cities found.")
    else:
        print("Error fetching data.")

def fetch_weather(api_key, lat,long):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid={api_key}"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        print(f"Weather in {city}:")
        print(f"Description: {weather_description}")
        print(f"Temperature: {temperature-273}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("Error fetching weather data.")

if __name__== "__main__":
    api_key = 'bb11ea1bd76426ae0856f6337b19c2cd'
    city = input("Enter city name: ")
    fetch_coordinates(api_key,city)