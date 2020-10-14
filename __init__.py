from mycroft import MycroftSkill, intent_file_handler


class SpotifySonosBot(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('bot.sonos.spotify.intent')
    def handle_bot_sonos_spotify(self, message):
        self.speak_dialog('bot.sonos.spotify')


def create_skill():
    return SpotifySonosBot()

