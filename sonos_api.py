import requests
from slugify import slugify
from mycroft.util import LOG


API_URL="http://localhost:5005/"
DELTA_VOLUME = 5


def play(speaker):
    requests.get(API_URL + speaker + '/' + 'play')


def stop(speaker):
    requests.get(API_URL + speaker + '/' + 'pauseall')


def set_volume(speaker, wanted_volume):
    requests.get(API_URL + speaker + '/' + 'volume/' + wanted_volume)


def increase_volume(speaker):
    requests.get(API_URL + speaker + '/' + 'volume/+' + DELTA_VOLUME)


def decrease_volume(speaker):
    requests.get(API_URL + speaker + '/' + 'volume/-' + DELTA_VOLUME)


def search_and_play_album(speaker, album_name):
    url = API_URL + speaker + '/musicsearch/spotify/album/' + \
          slugify(album_name)
    LOG.info(url)
    requests.get(url)


def search_and_play_playlist(speaker, playlist_name):
    url = API_URL + speaker + '/musicsearch/spotify/playlist/' + \
          slugify(playlist_name)
    LOG.info(url)
    requests.get(url)
