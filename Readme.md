Code Description
This Python script retrieves geographic coordinates and current weather data for a specified city using the OpenWeatherMap API. It consists of two main functions: fetch_coordinates and fetch_weather.

Functionality Breakdown
Imports:

The script starts by importing the requests library, which is used to make HTTP requests to external APIs.
fetch_coordinates(api_key, city):

This function takes an API key and a city name as inputs.
It constructs a URL for the OpenWeatherMap geocoding API to fetch latitude and longitude for the specified city.
It sends a GET request to the API and processes the JSON response.
If the response is successful (status_code == 200) and contains data:
It iterates through the results (up to five) and prints the city's name along with its latitude and longitude.
It then calls the fetch_weather function to retrieve and display weather information for the coordinates.
If no matching cities are found or if there is an error in fetching data, it prints an appropriate message.
fetch_weather(api_key, lat, long):

This function is responsible for retrieving current weather data based on the provided latitude and longitude.
It constructs a URL for the OpenWeatherMap current weather API.
It sends a GET request to fetch weather information and processes the JSON response.
If the response is successful:
It extracts and prints the weather description, temperature (converted from Kelvin to Celsius), humidity, and wind speed.
If an error occurs during data fetching, it prints an error message.
Main Execution Block:

The script checks if it is being run as the main program.
It prompts the user to enter a city name.
The provided API key (which should be kept secure) is passed along with the city name to the fetch_coordinates function to initiate the data retrieval process.
Key Points:
API Key: The script uses an API key to access OpenWeatherMap's services. This key should be kept confidential and not shared publicly.
Error Handling: Basic error handling is implemented to handle potential issues during API calls, such as invalid city names or network errors.
Unit Conversion: The temperature is converted from Kelvin to Celsius before being displayed.
User Interaction: The script interacts with the user through the command line, prompting them to enter a city name.
Usage:
To use this script, you need to have a valid OpenWeatherMap API key and the requests library installed in your Python environment. You can run the script, input a city name, and it will display the city's coordinates and current weather information.

This script is a practical example of how to integrate external APIs in Python to fetch and display real-time data.



