from mycroft import MycroftSkill, intent_file_handler
from .sonos_api import (
    play,
    stop,
    search_and_play_album,
    search_and_play_playlist,
)


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
    def play(self, message):
        stop(self.default_speaker)

    @intent_file_handler('play_album.intent')
    def play_album(self, message):
        album_name = message.data.get('album_name')
        self.log.info(message.data)
        if album_name:
            search_and_play_album(self.default_speaker, album_name)
        else:
            self.speak('Please try again with an album name')

    @intent_file_handler('play_playlist.intent')
    def play_playlist(self, message):
        playlist_name = message.data.get('playlist_name')
        if playlist_name:
            search_and_play_playlist(self.default_speaker, playlist_name)
        else:
            self.speak('Please try again with a playlist name')



def create_skill():
    return SpotifySonosBot()
