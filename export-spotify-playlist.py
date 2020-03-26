from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import json

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

playlist_id = 'spotify:user:redmusicompany:playlist:4joqw3e0n9gDNVDhgKapCU'
results = sp.playlist(playlist_id)
print(json.dumps(results, indent=4))


