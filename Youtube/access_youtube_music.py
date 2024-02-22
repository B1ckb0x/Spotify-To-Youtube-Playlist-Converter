from ytmusicapi import YTMusic

ytmusic = YTMusic("oauth.json")

playlistId = ytmusic.create_playlist("test", "test description")

search_results = ytmusic.search("car radio by twenty one pilots", "songs")

# ytmusic.add_playlist_items(playlistId, [search_results[0]['videoId']])

# Extract relevant information from the search results
songs_info = [{'title': song['title'], 'videoId': song['videoId']} for song in search_results]

# Find the text before "by" in the search query
# Used "by" to improve youtube music search as it was giving remix of the songs before
query = ""
index_of_by = query.find(" by ")
search_text = query[:index_of_by] if index_of_by != -1 else query

# Find the corresponding video ID
video_id = None
for song in songs_info:
    if search_text in song['title']:
        video_id = song['videoId']
        break

if video_id:
    ytmusic.add_playlist_items(playlistId, [video_id])
    print("Song added to playlist")
else:
    print("Song not found")
