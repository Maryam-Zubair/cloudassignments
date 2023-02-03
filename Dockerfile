FROM python:3.10

WORKDIR /weatherapp

COPY . .

RUN pip install -r requirements.txt

CMD [ "python", "weather.py"]