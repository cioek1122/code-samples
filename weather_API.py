import requests

API_KEY = "e74a9e431157a499ee0b910b68ab671a"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url= f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)


if response.status_code == 200:
    data = response.json()
    weather = data["weather"][0]["description"]
    temperature = (1.8 * ((data["main"]["temp"])-273) +32)
    print("Weather: ", weather)
    print("{:0.2f}".format(temperature), "Fahrenheit")
else:
    print("An error occured.")
