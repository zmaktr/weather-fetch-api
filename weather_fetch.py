from urllib import response
import requests

API_KEY     = '28c88a4a0b65728feaa241357c163062'
CITY        = input('Enter city? ')
BASE_URL    = 'https://api.openweathermap.org/data/2.5/weather'


request_url = f"{BASE_URL}?q={CITY}&appid={API_KEY}"

response    = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    print(data)
    weather = data['weather']["description"]
    print(weather)
else:
    print("An error occured while processing")
