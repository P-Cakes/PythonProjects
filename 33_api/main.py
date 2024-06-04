import requests
from datetime import datetime

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
# 404 response code means it doesn't exist
# 1xx : hold on, something's happening
# 2xx: here you go
# 3xx: go away
# 4xx: you screwed up
# 5xx: I screwed up

data = response.json()
longitude = float(data["iss_position"]["longitude"])
latitude = float(data["iss_position"]["latitude"])
iss_position = (longitude, latitude)
print(iss_position)
my_lat = 40.7989
my_long = -74.1886


response2 = requests.get(
    url="https://api.sunrise-sunset.org/json",
    params={
        "lat": my_lat,
        "lng": my_long,
        "formatted": 0
    })
response2.raise_for_status()
data2 = response2.json()
sunrise = data2["results"]["sunrise"].split("T")[1]
sunset = data2["results"]["sunset"].split("T")[1]
print(f"My sunrise is at {sunrise} and sunset is at {sunset}.")


time_now = datetime.now()
print(time_now)

# Need to convert the utc time to local time
# subtract 4 hours from utc time to get local time
sunrise_hour = int( sunrise.split(":")[0]) -4
sunset_hour = int (sunset.split(":")[0] ) -4
if sunrise_hour < 0:
    sunrise_hour += 24
if sunset_hour < 0:
    sunset_hour += 24

if int(sunrise_hour) < time_now.hour < int(sunset_hour) :
    print("It's daytime.")
else:
    print("It's nighttime.")

# If currently dark, check if ISS is overhead
if int(sunset_hour) < time_now.hour < int(sunrise_hour):
    if my_lat - 5 <= latitude <= my_lat + 5 and my_long - 5 <= longitude <= my_long + 5:
        print("Look up! The ISS is overhead.")
    else:
        if my_lat - 5 <= latitude <= my_lat + 5 and my_long - 5 <= longitude <= my_long + 5:
            print ("The ISS is close but it is light out.")
        else:
            print("The ISS is not overhead.")


# If dark and ISS is overhead, send an email
# import smtplib
# import os
# import ssl

#Improve further by changing the ifs to a function
# automate the function triggering
# update function to send emails



