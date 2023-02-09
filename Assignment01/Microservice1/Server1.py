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
        return {"Zip code": zip_code} 
        # weather_response = requests.get(f"http://service2:8081/weather?zip_code={zip_code}")
    else:
        return {"error": "zip code not found for city '{}'".format(city)}

        # instead of returning zipcode he is also calling out servis 2 url
   
if __name__ == "__main__":
    app.run(port=3000)