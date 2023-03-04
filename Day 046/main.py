#TODO 1: Tạo file main.py
#TODO 2: Create an input() prompt that asks what year you would like to travel to in YYY-MM-DD format. e.g.
#TODO 3: Using what you've learnt about BeautifulSoup, scrape the top 100 song titles on that date into a Python List.
#TODO 4: Set authen with spotify
#TODO 5: Get ID and Auth
#TODO 6: Get All list song
#TODO 7: Create playlist and add list link for playlist

from datetime import datetime
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials

s = str(input('Which year do you want to travel to? Type the date in the format YYYY-MM-DD: '))

soup = BeautifulSoup(requests.get(f'https://www.billboard.com/charts/hot-100/{s}/').text, "html.parser")
list_song = [str(i.string).strip() for i in soup.find_all("h3", {"id": "title-of-a-story", 'class' : lambda x: x and 'c-title' and 'a-no-trucate' in x.split()})]

p1 = spotipy.Spotify(auth_manager=spotipy.oauth2.SpotifyOAuth(show_dialog="True", scope="playlist-modify-public", redirect_uri="http://localhost:8888/callback", client_id="79c373e9e3f94fb1b53e5f0a548a33cb", client_secret="f202593d66e94f0c8781a8858d6ee101"))
results = p1.current_user()['id']
list_id_song = []
for i in list_song:
    try:
        a = p1.search(q=f"track:{i}", type="track")
        list_id_song.append(a["tracks"]["items"][0]["uri"])
    except:
        continue
aaa = p1.user_playlist_create(user=f"{results}", name=f"{s} Billboard 100", public=True, description=f"Top Tracks in {s}")
p1.playlist_add_items(playlist_id=aaa['id'], items=list_id_song)

