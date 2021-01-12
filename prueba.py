import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

print(spotify.user(spotify.me()))
#albums = results['items']
#while results['next']:
#    results = spotify.next(results)
#    albums.extend(results['items'])
#
#for album in albums:
#    print(album['name'])