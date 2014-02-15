import os
import requests
import bollywood

API_KEY = os.environ['YOUTUBE_API_KEY']
DATA_BASE_URL = 'https://www.googleapis.com/youtube/v3/search'
VIDEO_URL = 'http://www.youtube.com/watch?v=%s'
SEARCH_ORDER = 'relevance'
SEARCH_TYPE = 'video'
SEARCH_PART = 'snippet'

def make_search_query(terms):
    return '+'.join(terms).replace(' ', '+')

def perform_search(search_query):
    return requests.get(DATA_BASE_URL, params={
        'part': SEARCH_PART,
        'q': search_query,
        'order': SEARCH_ORDER,
        'type': SEARCH_TYPE,
        'key': API_KEY
    }).json()

def get_video_id(video_item):
    return video_item['id']['videoId']

def get_video_url(search_results):
    items = search_results['items']
    if len(items) == 0:
        return None
    return VIDEO_URL % get_video_id(items[0])

def find_song(song_name):
    song_info = bollywood.get_song(song_name)

    canonical_song_name = song_info['Name']
    artists = song_info['Singers']

    search_results = perform_search(make_search_query([
        canonical_song_name
    ]))

    return get_video_url(search_results)

def find_movie_soundtrack(movie_name):
    movie_info = bollywood.get_album(movie_name)
    song_names = [song['Name'] for song in movie_info['Songs']]

    results = []
    for song_name in song_names:
        song = find_song(song_name)
        if song is not None:
            results.append(song)
    return results
