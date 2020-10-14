from mycroft import MycroftSkill, intent_file_handler
from .sonos_api import (
    play,
    stop,
)


class SpotifySonosBot(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.default_speaker = None

    def initialize(self):
        self.settings_change_callback = self.on_settings_changed
        self.on_settings_changed()

    def on_settings_changed(self):
        self.default_speaker = self.settings.get('default_speaker')

    def stop(self):
        stop(self.default_speaker)

    @intent_file_handler('play_any_music.intent')
    def play(self, message):
        play(self.default_speaker)


def create_skill():
    return SpotifySonosBot()
