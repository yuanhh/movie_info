from __future__ import absolute_import
from __future__ import print_function

import requests

__key__ = '0df993c66c0c636e29ecbb5344252a4a'

class URL:
    def __init__(self):
        self.imdb = 'http://api.douban.com/v2/movie/imdb/{imdb_id}?apiKey={api_key}'
        self.search = 'http://api.douban.com/v2/movie/search?apiKey={api_key}&q={q}&count=1'

class Douban:
    def __init__(self):
        self.url = URL()

    def get(self, **kwargs):
        response = requests.request('GET', self.url.imdb.format(
            imdb_id = kwargs['imdb_id'],
            api_key = __key__
        ))
        if response is None:
            return None

        response = response.json()

        attr = response.get('attrs')
        if attr is None:
            return None

        movie_type = attr.get('movie_type')

        return {
            'imdb_id': kwargs['imdb_id'],
            'movie_type': movie_type,
            'title': {
                'en': response['title'],
                'ch': response['alt_title'][:response['alt_title'].find('/') - 1],
                'hk': response['alt_title'][response['alt_title'].find('/') + 2: -3]
            }
        }
