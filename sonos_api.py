import requests
from slugify import slugify
from mycroft.util import LOG


API_URL="http://localhost:5005/"


def play(speaker):
    requests.get(API_URL + speaker + '/' + 'play')


def stop(speaker):
    requests.get(API_URL + speaker + '/' + 'pauseall')


def volume(speaker, volume):
    requests.get(API_URL + speaker + '/' + 'volume/' + volume)


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
