# import flask  
from flask import Flask
import json
import requests
import config

# create flask app

app = Flask(__name__)

# create route for index page

@app.route('/')
def index():
    return "hello world"

# create a route that takes a city name as a parameter

@app.route('/<city>')
def weather(city):
    zip_code = get_zip_code(city)
    weather = get_weather(zip_code)
    weather = weather["main"]["temp"]
    weather = round((weather - 273.15) * 9/5 + 32,2)
    return f"The temperature in {city} is {weather} F"

# create a function that takes a city name and returns the zip code

def get_zip_code(city):
    response = requests.get(f"https://www.zipcodeapi.com/rest/DemoOnly00T9TlNMaZIPoG6Z81oPYYCUF8EkrAmhdri9QZIj2zXaLg3vU5sQAIFG/city-zips.json/{city}/CA")
    zip_code = json.loads(response.text)['zip_codes']
    if len(zip_code) > 0:
        zip_code = zip_code[0]
    else:
        return get_zip_code("san-francisco")
    return zip_code

# create a function that takes a zip code and returns the weather

def get_weather(zip_code):
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?zip={zip_code}&appid={config.api_key}")
    weather = json.loads(response.text)
    return weather

if __name__ == "__main__":
    app.run(port=3000, debug=True)