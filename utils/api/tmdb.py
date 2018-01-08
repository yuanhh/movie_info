from __future__ import absolute_import
from __future__ import print_function

import requests

__key__ = '368858ba0976e216625527ac96a9f52d'

class URL:
    def __init__(self):
        self.get = 'https://api.themoviedb.org/3/movie/{movie_id}'
        self.find = 'https://api.themoviedb.org/3/find/{imdb_id}'
        self.search = 'https://api.themoviedb.org/3/search/movie'

class TMDB:
    def __init__(self):
        self.url = URL()

    def search(self, **kwargs):
        # var
        payload = {
            'api_key': __key__,
            'language': 'en-US',
            'query': kwargs['query'],
            'include_adult': True
        }

        response = requests.request('GET', self.url.search, data = payload)
        response = response.json()

        if len(response['results']) == 0:
            return None

        result = sorted(response['results'], key = lambda x: x['popularity'], reverse = True)

        return result[0]

    def get(self, **kwargs):
        payload = {
            'api_key': __key__,
            'language': 'en-US'
        }

        response = requests.request('GET', self.url.get.format(movie_id = kwargs['movie_id']), data = payload)

        return response.json()

    def find(self, **kwargs):
        # var
        payload = {
            'api_key': __key__,
            'external_id': kwargs['imdb_id'],
            'external_source': 'imdb_id'
        }

        response = requests.request('GET', self.url.find.format(imdb_id = kwargs['imdb_id']), data = payload)
        response = response.json()

        result = sorted(response['movie_results'], key = lambda x: x['popularity'], reverse = True)
        if len(result) == 0:
            return None

        return result[0]
