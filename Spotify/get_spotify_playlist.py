import json
import webbrowser

import requests
from bs4 import BeautifulSoup

from Spotify.get_api import api_needs_refresh

# file = "API/api.txt"

access_token = api_needs_refresh()
# print(access_token)

url = 'https://api.spotify.com/v1/playlists/36qx4wzHmjl8BRVWxDg4ph/tracks?fields=items%28track%28name%29%29'

headers = {
    'Authorization': f'Bearer {access_token}'
}

response = requests.get(url, headers=headers)
json_data = response.json()


track_names = [item['track']['name'] for item in json_data['items']]
print("Track Names: ", track_names)

with open('track_names.txt', 'w', encoding='utf-8') as file:
    for name in track_names:
        file.write(name + "\n")


# json_format = json.dumps(json_data, indent=2)
# html_content = f"<pre>{json_format}</pre>"
# soup = BeautifulSoup(html_content, 'html.parser')
#
# with open('output.html', 'w', encoding='utf-8') as file:
#     file.write(str(soup))
#
# webbrowser.open('output.html')
