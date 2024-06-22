
# use beautiful soup to scrape the top 100 songs from billboard

# Use Spotify API to create a playlist with the top 100 songs

import requests
from bs4 import BeautifulSoup
import datetime
import spotipy

import os
with open('spotify_cred.txt', 'r') as f:
    for line in f:
        if line.strip():  # ignore empty lines
            key, value = line.strip().split('=', 1)
            os.environ[key] = value

target_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
# check that the target date is in the correct format
# while len(target_date) != 10 or target_date[4] != "-" or target_date[7] != "-":
#     print("The date you entered is not in the correct format. Please enter a date in this format YYYY-MM-DD")
#     target_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
# # check that the target date is not in the future
# today_date = datetime.datetime.now().date()
# while target_date > today_date:
#     print("The date you entered is in the future. Please enter a date before 2021-09-14")
#     target_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{target_date}")
response.raise_for_status()
data = response.text

soup = BeautifulSoup(data, "html.parser")

song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
print (song_names)