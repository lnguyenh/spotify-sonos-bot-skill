from mycroft import MycroftSkill, intent_file_handler
from mycroft.util.parse import extract_number
from .sonos_api import (
    play,
    stop,
    search_and_play_album,
    search_and_play_playlist,
    increase_volume, decrease_volume, set_volume)


class SpotifySonosBot(MycroftSkill):
    def initialize(self):
        self.settings_change_callback = self.on_settings_changed
        self.on_settings_changed()

    def on_settings_changed(self):
        self.default_speaker = self.settings.get('default_speaker')
        self.log.info('Default speaker set to {}'.format(self.default_speaker))

    def stop(self):
        stop(self.default_speaker)

    @intent_file_handler('play_any_music.intent')
    def play(self, message):
        play(self.default_speaker)

    @intent_file_handler('stop_the_music.intent')
    def stop_(self, message):
        stop(self.default_speaker)

    @intent_file_handler('play_album.intent')
    def play_album(self, message):
        album_name = message.data.get('album_name')
        self.log.info(message.data)
        if album_name:
            search_and_play_album(self.default_speaker, album_name)

    @intent_file_handler('play_playlist.intent')
    def play_playlist(self, message):
        playlist_name = message.data.get('playlist_name')
        self.log.info(message.data)
        if playlist_name:
            search_and_play_playlist(self.default_speaker, playlist_name)

    @intent_file_handler('increase_volume.intent')
    def increase_volume(self, message):
        increase_volume(self.default_speaker)

    @intent_file_handler('decrease_volume.intent')
    def derease_volume(self, message):
        decrease_volume(self.default_speaker)

    @intent_file_handler('set_volume.intent')
    def set_volume(self, message):
        wanted_volume = message.data.get('wanted_volume', '')
        wanted_volume = extract_number(wanted_volume)
        self.log.info('{} {}'.format(message.data, wanted_volume))
        if wanted_volume:
            set_volume(self.default_speaker, str(wanted_volume))


def create_skill():
    return SpotifySonosBot()
