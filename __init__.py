from mycroft import MycroftSkill, intent_file_handler
from mycroft.util.parse import extract_number

from .spotify import SpotifyClient
from .sonos_api import (
    play,
    stop,
    search_and_play_album,
    search_and_play_playlist,
    increase_volume,
    decrease_volume,
    set_volume,
    next_song,
    previous,
    search_and_play_artist,
    play_playlist, queue_song, search_and_play_song, clear_queue, play_song)


class SpotifySonosBot(MycroftSkill):
    def initialize(self):
        self.settings_change_callback = self.on_settings_changed
        self.on_settings_changed()

    def on_settings_changed(self):
        self.speaker = self.settings.get('default_speaker')
        self.log.info('Default speaker set to {}'.format(self.speaker))
        self.spotify_username = self.settings.get('spotify_username')
        self.spotify_client_id = self.settings.get('spotify_client_id')
        self.spotify_client_secret = self.settings.get('spotify_client_secret')
        self.refresh_spotify()

    @property
    def spotify_ready(self):
        return  (self.spotify_username and self.spotify_client_secret and
                 self.spotify_client_id)

    def refresh_spotify(self):
        self.playlists = {}
        self.client = None
        if self.spotify_ready:
            try:
                self.client = SpotifyClient(self.spotify_client_id,
                                            self.spotify_client_secret)
                self.playlists = self.client.fetch_user_playlists(
                    self.spotify_username)
                self.log.info('Found %s playlists for user %s' % (
                    len(self.playlists), self.spotify_username))
            except Exception as e:
                self.log.warning('Could not fetch Spotify playlists for user '
                                 '%s: %s' % (self.spotify_username, e))

    def stop(self):
        stop(self.speaker)

    @intent_file_handler('play_any_music.intent')
    def play(self, message):
        play(self.speaker)

    @intent_file_handler('stop_the_music.intent')
    def stop_(self, message):
        stop(self.speaker)

    @intent_file_handler('play_album.intent')
    def play_album(self, message):
        album_name = message.data.get('album_name')
        self.log.info(message.data)
        if album_name:
            found = search_and_play_album(self.speaker, album_name)
            if not found:
                self.speak('There is no album called {}'.format(album_name))

    @intent_file_handler('play_song.intent')
    def play_song(self, message):
        song_name = message.data.get('song_name')
        self.log.info(message.data)
        if song_name:
            found = search_and_play_song(self.speaker, song_name)
            if not found:
                self.speak('There is no album called {}'.format(song_name))

    @intent_file_handler('play_playlist.intent')
    def play_playlist(self, message):
        playlist_name = message.data.get('playlist_name')
        self.log.info(message.data)
        if playlist_name:
            if playlist_name.lower() in self.playlists:
                self.log.info('Found playlist for user %s' %
                              self.spotify_username)
                play_playlist(self.speaker, self.playlists[playlist_name])
            else:
                found = search_and_play_playlist(self.speaker, playlist_name)
                if not found:
                    self.speak('There is no playlist called {}'.format(
                        playlist_name))

    @intent_file_handler('play_artist.intent')
    def play_artist(self, message):
        artist_name = message.data.get('artist_name')
        self.log.info(message.data)
        if artist_name:
            tracks = self.client.get_top_tracks(artist_name)
            clear_queue(self.speaker)
            for i, track_uri in enumerate(tracks):
                if i == 0:
                    play_song(self.speaker, track_uri)
                else:
                    queue_song(self.speaker, track_uri)

    @intent_file_handler('radio_artist.intent')
    def radio_artist(self, message):
        artist_name = message.data.get('artist_name')
        self.log.info(message.data)
        if artist_name:
            found = search_and_play_artist(self.speaker, artist_name)
            if not found:
                self.speak('There is no radio for artist called {}'.format(
                    artist_name))

    @intent_file_handler('refresh_spotify_playlists.intent')
    def refresh_spotify_playlists(self, message):
        self.refresh_spotify()

    @intent_file_handler('increase_volume.intent')
    def increase_volume(self, message):
        increase_volume(self.speaker)

    @intent_file_handler('decrease_volume.intent')
    def decrease_volume(self, message):
        decrease_volume(self.speaker)

    @intent_file_handler('set_volume.intent')
    def set_volume(self, message):
        wanted_volume = message.data.get('wanted_volume', '')
        wanted_volume = extract_number(wanted_volume)
        self.log.info('{} {}'.format(message.data, wanted_volume))
        if wanted_volume:
            set_volume(self.speaker, wanted_volume)

    @intent_file_handler('next_song.intent')
    def next_song(self, message):
        next_song(self.speaker)

    @intent_file_handler('previous_song.intent')
    def previous_song(self, message):
        previous(self.speaker)


def create_skill():
    return SpotifySonosBot()
