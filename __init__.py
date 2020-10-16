from mycroft import MycroftSkill, intent_file_handler
from mycroft.util.parse import extract_number
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
)


class SpotifySonosBot(MycroftSkill):
    def initialize(self):
        self.settings_change_callback = self.on_settings_changed
        self.on_settings_changed()

    def on_settings_changed(self):
        self.speaker = self.settings.get('default_speaker')
        self.log.info('Default speaker set to {}'.format(self.speaker))

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

    @intent_file_handler('play_playlist.intent')
    def play_playlist(self, message):
        playlist_name = message.data.get('playlist_name')
        self.log.info(message.data)
        if playlist_name:
            found = search_and_play_playlist(self.speaker, playlist_name)
            if not found:
                self.speak('There is no playlist called {}'.format(
                    playlist_name))

    @intent_file_handler('play_artist.intent')
    def play_artist(self, message):
        artist_name = message.data.get('artist_name')
        self.log.info(message.data)
        if artist_name:
            found = search_and_play_artist(self.speaker, artist_name)
            if not found:
                self.speak('There is no artist called {}'.format(artist_name))

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
