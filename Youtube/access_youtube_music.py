from ytmusicapi import YTMusic

ytmusic = YTMusic("oauth.json")

playlistId = ytmusic.create_playlist("test", "test description")
search_results = ytmusic.search("Fortnite Raise Up Lobby Music")
ytmusic.add_playlist_items(playlistId, [search_results[0]['videoId']])

print('Done')