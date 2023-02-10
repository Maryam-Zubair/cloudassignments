from flask import Flask, request
from pyzipcode import ZipCodeDatabase
import requests

app = Flask(__name__)
zcdb = ZipCodeDatabase()

# @app.route("/zipcode", methods=["GET"])
@app.route("/zipcode", methods=["GET"])
def get_zip_code():

    city = request.args.get("city")
    zip_code = zcdb.find_zip(city=city)
    # return {"zip_code": zip_code[0].zip }

    if zip_code:
        for zc in zip_code:
            zip_code = zc.zip
            break
        # return {"Zip code": zip_code} 
        weather_response = requests.get(f"http://zipcode:3001/check_weather?zip_code={zip_code}")
        if weather_response.status_code == 200:
            return weather_response.text

        # instead of returning zipcode he is also calling out servis 2 url
   
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)