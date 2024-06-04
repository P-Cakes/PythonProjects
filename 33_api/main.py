import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
# 404 response code means it doesn't exist
# 1xx : hold on, something's happening
# 2xx: here you go
# 3xx: go away
# 4xx: you screwed up
# 5xx: I screwed up

data = response.json()
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
iss_position = (longitude, latitude)
print(iss_position)
