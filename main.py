import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

load_dotenv()

spotify_url = "https://api.spotify.com/v1/users/{user_id}/playlists"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.environ.get("SPOTIPY_CLIENT_ID"),
    client_secret=os.environ.get("SPOTIPY_CLIENT_SECRET"),
    redirect_uri="http://127.0.0.1:8888/callback",
    scope="playlist-modify-public playlist-modify-private"
))

# Get the authenticated user's Spotify ID
user_info = sp.current_user()
user_id = user_info['id']
print(f"Authenticated Spotify user ID: {user_id}")

user_input = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

playlist_name = f"{user_input} Billboard 100"
playlist_id = None
results = sp.current_user_playlists()
for item in results['items']:
    if item['name'] == playlist_name:
        playlist_id = item['id']
        print(f"Found existing playlist: {playlist_name}")
        break

# If not found, create a new playlist
if not playlist_id:
    playlist = sp.user_playlist_create(
        user=user_id,
        name=playlist_name,
        public=False,
        description="Most popular songs"
    )
    playlist_id = playlist['id']
    print("Created playlist:", playlist['name'])

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

URL = f"https://www.billboard.com/charts/hot-100/{user_input}/"
response = requests.get(URL, headers=header)
response.raise_for_status()
song_page = response.text

soup = BeautifulSoup(song_page, "html.parser")
# Find only song titles (usually inside li tags with chart-element__information)
song_titles = []
for title in soup.find_all("h3", class_="c-title"):
    parent = title.find_parent("li")
    if parent and parent.get("class") and "o-chart-results-list__item" in parent.get("class"):
        song_titles.append(title.getText().strip())

print(f"Found {len(song_titles)} song titles.")
print(song_titles[:20])  # Print the first 20 song titles for verification

spotify_uris = []
for idx, title in enumerate(song_titles):
    print(f"Searching Spotify for: {title} ({idx+1}/{len(song_titles)})")
    result = sp.search(q=title, type='track', limit=1)
    tracks = result['tracks']['items']
    if tracks:
        uri = tracks[0]['uri']
        spotify_uris.append(uri)
    else:
        print(f"No Spotify track found for: {title}")

# Only playlist_id and tracks are needed
add_tracks = sp.playlist_add_items(
    playlist_id=playlist_id,
    items=spotify_uris
)
print("Spotify URIs:", spotify_uris)


