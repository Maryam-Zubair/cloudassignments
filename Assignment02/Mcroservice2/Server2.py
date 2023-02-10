from flask import Flask, request
import requests
import config

app = Flask(__name__)

@app.route("/check_weather", methods=["GET"])
def get_weather():
    zip_code = request.args.get("zip_code")
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?zip={zip_code},us&appid={config.api_key}"
    response = requests.get(weather_url) 

    if response.status_code == 200:
        weather_data = response.json() 
        description = weather_data["weather"][0]["main"]
        kelvin_weather = weather_data["main"]["temp"]
        temp = kelvin_to_fahrenheit(kelvin_weather)
        city = weather_data["name"]

        return (
            f'City: {city}  ,  Weather Desciption: {description} ,  Temperature: {temp}F '
        )   
    else:
        return response.json()
     
def kelvin_to_fahrenheit(temp_kelvin):
    temp_fahrenheit = (temp_kelvin - 273.15) * 9/5 + 32
    return round(temp_fahrenheit)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3001, debug=True)