import requests

my_lat = 40.7989
my_long = -74.1886
api_key = "3f304717f619fda0c7bd8d14fe9e91f9"

api_url = "https://api.openweathermap.org/data/2.5/forecast"
api_params = {
    "lat": my_lat,
    "lon": my_long,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(url = api_url, params = api_params )
response.raise_for_status()
data = response.json()

for forecast in data['list']:
    # print ((forecast['dt_txt'],forecast['weather']))
    if forecast['weather'][0]['id'] < 700:
        print(f"Bring an umbrella on {forecast['dt_txt']}.")