import requests
from slugify import slugify
from mycroft.util import LOG


API_URL="http://localhost:5005/"
DELTA_VOLUME = '5'


def get(url):
    LOG.info(url)
    requests.get(url)

def play(speaker):
    get(API_URL + speaker + '/' + 'play')


def stop(speaker):
    get(API_URL + speaker + '/' + 'pauseall')


def set_volume(speaker, wanted_volume):
    get(API_URL + speaker + '/' + 'volume/' + wanted_volume)


def increase_volume(speaker):
    get(API_URL + speaker + '/' + 'volume/+' + DELTA_VOLUME)


def decrease_volume(speaker):
    get(API_URL + speaker + '/' + 'volume/-' + DELTA_VOLUME)


def search_and_play_album(speaker, album_name):
    get(API_URL + speaker + '/musicsearch/spotify/album/' +
        slugify(album_name))


def search_and_play_playlist(speaker, playlist_name):
    get(API_URL + speaker + '/musicsearch/spotify/playlist/' +
        slugify(playlist_name))
