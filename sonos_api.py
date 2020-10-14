import requests


API_URL="http://localhost:5005/"


def play(speaker):
    requests.get(API_URL + speaker + '/' + 'play')


def stop(speaker):
    requests.get(API_URL + speaker + '/' + 'pauseall')


def volume(speaker, volume):
    requests.get(API_URL + speaker + '/' + 'volume/' + volume)


def search_and_play_album(speaker, album_name):
    requests.get(API_URL + speaker + '/' + '/musicsearch/spotify/' +
                 album_name)
