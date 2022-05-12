import requests
import os
from twilio.rest import Client

MY_LAT = 51.209179
MY_LNG = -2.645860

account_sid = 'AC69c71f6846a184bdd1830ff00b1c8ffd'
auth_token = '7e887db4625181dd21e22b098e559342'


API_KEY = '17be7456176b91327a3630d4be92b451'
URL = 'https://api.openweathermap.org/data/2.5/onecall'
parameters = {
    'lat': MY_LAT,
    'lon': MY_LNG,
    'appid': API_KEY,
    'exclude':'current,minutely,daily',
}

respond = requests.get(url=URL , params= parameters)
respond.raise_for_status()
weather_data = respond.json()

weather_data_num = [weather_data['hourly'][i]['weather'][0]['id'] for i in range(12)]
will_rain = False

for i in range(int(len(weather_data_num))):
    if weather_data_num[i] < 700:
        will_rain = True
    else:
        pass

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body="IT is gona rain take an umbrella !!!",
                     from_='+16292224661',
                     to='+905323783032'
                 )

    print(message.status)