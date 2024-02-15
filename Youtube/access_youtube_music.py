from ytmusicapi import YTMusic

ytmusic = YTMusic("oauth.json")

playlistId = ytmusic.create_playlist("test", "test description")
# search_results = ytmusic.search("Fortnite Raise Up Lobby Music")
search_results = [{'videoId': '6io0g7WuHaI'}]
ytmusic.add_playlist_items(playlistId, [search_results[0]['videoId']])

print('Done')


# When I search for a music on YouTube music it shows id after watch ,
# that is what I will use, I just need to find it in the list that it give me

