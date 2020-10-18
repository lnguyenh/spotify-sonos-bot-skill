import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


class SpotifyClient(object):
    def __init__(self, client_id, client_secret):
        os.environ['SPOTIPY_CLIENT_ID'] = client_id
        os.environ['SPOTIPY_CLIENT_SECRET'] = client_secret
        auth_manager = SpotifyClientCredentials()
        self.spotipy_client = spotipy.Spotify(auth_manager=auth_manager)

    def fetch_user_playlists(self, username):
        playlists = {}
        raw_playlists = self.spotipy_client.user_playlists(username, limit=100)
        if raw_playlists and raw_playlists.get('items'):
            playlists = {
                playlist['name'].lower(): playlist['uri']
                for playlist in raw_playlists['items']
            }
        return playlists
