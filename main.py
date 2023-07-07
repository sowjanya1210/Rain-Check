import requests
from twilio.rest import Client
api_key = "ed0f7cfb7dfa4a88eaab66b222d4e74c"
account_sid = "AC8dcdae1149bf5736d82d49703ef37eca"
account_token = "953dad145f4c95f9559686ca28f32e1c"

parameters = {
    "q": "Krasnodar",
    "appid": api_key,
    "units": "metric",
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/weather", params=parameters)
print(response.json())

data = response.json()
id = int(data["weather"][0]["id"])
if id < 700:
    client = Client(account_sid, account_token)
    message = client.messages \
        .create(
        body="Bring an umbrella☂️as it is going to rain🌧️",
        from_="+16206784283",
        to="+918331966560"
    )
    print(message.status)
