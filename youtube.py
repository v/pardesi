import os
import requests
import bollywood

API_KEY = os.environ['YOUTUBE_API_KEY']
DATA_BASE_URL = 'https://www.googleapis.com/youtube/v3/search'

# CLIENT_ID = '40956099481-vsgv6b45mqeem7dcfn6hq4u13kt0n9ng.apps.googleusercontent.com';
# CLIENT_SECRET = 'JQgOjX1Kgh1kO4l0qfimjYqM';

def make_search_query(terms):
    return '+'.join(terms).replace(' ', '+')

def perform_search(search_query):
    return requests.get(DATA_BASE_URL, params={
        'part': 'snippet',
        'q': search_query,
        'key': API_KEY
    }).json()

def get_video_url(search_results):
    pass

def find_song(song_name):
    song_info = bollywood.get_song(song_name)

    canonical_song_name = song_info['Name']
    artists = song_info['Singers']

    search_results = perform_search(make_search_query([canonical_song_name] + artists))

    return get_video_url(search_results)

def find_movie_soundtrack(movie_name):
    movie_info = bollywood.get_album(movie_name)
    songs = [song['Name'] for song in movie_info['Songs']]

    results = []
    for song in songs:
        results.append(find_song(song))
    return results
