import requests

from Spotify.get_api import api_needs_refresh

access_token = api_needs_refresh()

url = 'https://api.spotify.com/v1/playlists/36qx4wzHmjl8BRVWxDg4ph/tracks?fields=items%28track%28name%2Cartists%28name%29%29%29'

headers = {
    'Authorization': f'Bearer {access_token}'
}

response = requests.get(url, headers=headers)
json_data = response.json()

# Extract track names and artist names and concatenate them
track_artist_pairs = [f"{item['track']['name']} by {item['track']['artists'][0]['name']}" for item in
                      json_data['items']]

# Write track names and artist names to a file
with open('track_artist_pairs.txt', 'w', encoding='utf-8') as file:
    for pair in track_artist_pairs:
        file.write(f"{pair}\n")
