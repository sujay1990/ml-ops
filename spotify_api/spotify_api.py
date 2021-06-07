import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
client_id = "1eab65ddaa724365933814d7cb58283e"
client_secret = "f296c7e16d6940b1b13317f1638ad44f"
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

name = ["Micheal Jackson","pitbull","Christina","Elvis Presley"]
result = sp.search(name)
result['tracks']['items'][1]['artists']

# Extract Artist's uri
artists_uris = result['tracks']['items'][0]['artists'][0]['uri']
# Pull all of the artist's albums
artist_albums = sp.artist_albums(artists_uris, album_type='album')
# Store artist's albums' names' and uris in separate lists
artist_album_names = []
artist_album_uris = []
for i in range(len(artist_albums['items'])):
    artist_album_names.append(artist_albums['items'][i]['name'])
    artist_album_uris.append(artist_albums['items'][i]['uri'])

print(artist_album_names)
print(artist_album_uris)
# Keep names and uris in same order to keep track of duplicate albums

