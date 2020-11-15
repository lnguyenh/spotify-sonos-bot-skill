import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


CHUNK_SIZE = 50


class SpotifyClient(object):
    def __init__(self, client_id, client_secret):
        os.environ['SPOTIPY_CLIENT_ID'] = client_id
        os.environ['SPOTIPY_CLIENT_SECRET'] = client_secret
        auth_manager = SpotifyClientCredentials()
        self.spotipy_client = spotipy.Spotify(auth_manager=auth_manager)

    def fetch_user_playlists(self, username):
        offset = 0

        results = self.spotipy_client.user_playlists(
            username, limit=CHUNK_SIZE, offset=offset)
        next_ = results['next']
        playlists = {
            playlist['name'].lower(): playlist['uri']
            for playlist in results['items']
        }

        while next_:
            results = self.spotipy_client.user_playlists(
                username, limit=CHUNK_SIZE, offset=offset)
            next_ = results['next']
            playlists_chunk = {
                playlist['name'].lower(): playlist['uri']
                for playlist in results['items']
            }
            playlists.update(playlists_chunk)
            offset = offset + CHUNK_SIZE

        return playlists

    def get_top_tracks(self, artist_name):
        artists = self.spotipy_client.search(
            q='artist:' + artist_name, type='artist')['artists']['items']

        if not artists:
            return []

        artist_id = artists[0]['id']
        tracks = self.spotipy_client.artist_top_tracks(artist_id)['tracks']

        if not tracks:
            return []
        else:
            return [track['uri'] for track in tracks]
