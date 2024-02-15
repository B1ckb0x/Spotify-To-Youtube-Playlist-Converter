import datetime
import os

import requests

PATH = '../API/api.txt'


def api_needs_refresh(file_path=PATH):
    # Check file modification time to compare with current time to check if api is expired
    modification_time = os.path.getmtime(file_path)
    dt_m = datetime.datetime.fromtimestamp(modification_time)
    # print(f"Modified on: {dt_m}")

    current_time = datetime.datetime.now()
    # print(current_time)

    time_difference = current_time - dt_m
    # print(time_difference)

    if time_difference.total_seconds() > 3000:
        get_spotify_access_token()
    else:
        #print("Can still use file")
        with open(file_path) as file:
            return file.read()

    """
        TO UNDERSTAND MYSELF
        if True - calls spotify request api - updates the file - returns the API
        else False - reads the file - returns the API
    """


# Gets a new access token from spotify if current one has expired
# This is called from the api_needs_refresh if the current file mod time is more than 50 minutes
def get_spotify_access_token():
    # API endpoint URL
    url = 'https://accounts.spotify.com/api/token'

    # Send POST request of our information and get the access token

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    data = {
        'grant_type': 'client_credentials',
        'client_id': '0e950b34525f40d5bd41fc110becb265',
        'client_secret': '99f2c3ce803c44ed9d9eb17783e72c83'
    }

    response = requests.post(url, headers=headers, data=data)

    # Get access token from response
    if response.status_code == 200:
        token_data = response.json()
        access_token = token_data.get('access_token')
        print("Access token:", access_token)

        try:
            with open("../API/api.txt", 'w+') as file:
                file.write(access_token)
                return file.read()
        finally:
            print("API in 'api.txt' file")

    else:
        print("Error:", response.status_code, response.text)


api_needs_refresh(PATH)
# Still testing pycharm
