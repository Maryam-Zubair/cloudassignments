FROM python:3.10

WORKDIR /Server1

COPY . .

RUN pip install -r requirements.txt

CMD [ "python", "Server1.py","--port=3000" ]