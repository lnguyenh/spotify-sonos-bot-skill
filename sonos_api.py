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
               slugify(album_name, separator='+'))


def search_and_play_song(speaker, song_name):
    return get(API_URL + speaker + '/musicsearch/spotify/song/' +
               slugify(song_name, separator='+'))

def search_and_play_playlist(speaker, playlist_name):
    return get(API_URL + speaker + '/musicsearch/spotify/playlist/' +
               slugify(playlist_name, separator='+'))


def search_and_play_artist(speaker, artist_name):
    return get(API_URL + speaker + '/musicsearch/spotify/station/' +
               slugify(artist_name, separator='+'))


def play_playlist(speaker, playlist_uri):
    # uri should look like spotify:playlist:5Sxw4p4AImvYJE36xe8UCr
    return get(API_URL + speaker + '/spotify/now/spotify:user:' +
               playlist_uri)


def queue_song(speaker, song_uri):
    return get(API_URL + speaker + '/spotify/queue/' + song_uri)


def play_song(speaker, song_uri):
    return get(API_URL + speaker + '/spotify/now/' + song_uri)


def clear_queue(speaker):
    return get(API_URL + speaker + '/clearqueue')


def get_state(speaker):
    return get(API_URL + speaker + '/state')


def get_volume(speaker):
    state = get_state(speaker)
    return state['volume']


def get_current_track(speaker):
    state = get_state(speaker)
    if state['currentTrack']['title']:
        return f"{state['currentTrack']['title']} by " \
            f"{state['currentTrack']['artist']}"
    else:
        return ''
