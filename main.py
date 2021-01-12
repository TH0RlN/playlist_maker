import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def main():
	#birdy_uri = 'spotify:artist:1tZ99AnqyjgrmPwLfGU5eo'
	q = f"track:{input('Búsqueda: ')}"
	spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

	results = spotify.search(q, limit=50, offset=0, type='track', market='ES')
	print(results)
#	tracks = results['tracks']['items']
#	
#	
#	for track in tracks:
#		print(track['name'])
#		#print("\n\n\n")
	#spotify.user_playlist_create("raul_ubl6", "lista de prueba", public=True, collaborative=False, description='')



if __name__ == '__main__':
	main()
#playlist_add_items(playlist_id, items, position=None)

