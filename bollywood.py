import requests

BASE_URL = 'http://www.bollywoodapi.com/v1'

GET_SONG = '/search/songs/%s'
GET_ALBUM = '/search/albums/%s'

def make_api_call(path):
    return requests.get(BASE_URL + path).json()

def get_song(song_name):
    songs = make_api_call(GET_SONG % song_name)
    return songs[0] if len(songs) > 0 else None

def get_album(album_name):
    albums = make_api_call(GET_ALBUM % album_name)
    return albums[0] if len(albums) > 0 else None
