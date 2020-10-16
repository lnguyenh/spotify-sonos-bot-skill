import requests
from slugify import slugify
from mycroft.util import LOG


API_URL="http://localhost:5005/"
MAX_VOLUME = 32
DELTA_VOLUME = 5


def get(url):
    LOG.info(url)
    response = requests.get(url)
    return response.ok

def play(speaker):
    return get(API_URL + speaker + '/' + 'play')


def stop(speaker):
    return get(API_URL + speaker + '/' + 'pauseall')


def next_song(speaker):
    return get(API_URL + speaker + '/' + 'next')


def previous(speaker):
    return get(API_URL + speaker + '/' + 'previous')


def set_volume(speaker, wanted_volume):
    if wanted_volume > MAX_VOLUME:
        LOG.info('Max volume exceeded. Wanted {}, max volume is {}')
        wanted_volume = MAX_VOLUME
    return get(API_URL + speaker + '/' + 'volume/' + str(wanted_volume))


def increase_volume(speaker):
    return get(API_URL + speaker + '/' + 'volume/+' + str(DELTA_VOLUME))


def decrease_volume(speaker):
    return get(API_URL + speaker + '/' + 'volume/-' + str(DELTA_VOLUME))


def search_and_play_album(speaker, album_name):
    return get(API_URL + speaker + '/musicsearch/spotify/album/' +
               slugify(album_name))


def search_and_play_playlist(speaker, playlist_name):
    return get(API_URL + speaker + '/musicsearch/spotify/playlist/' +
               slugify(playlist_name))


def search_and_play_artist(speaker, artist_name):
    return get(API_URL + speaker + '/musicsearch/spotify/artist/' +
               slugify(artist_name))
