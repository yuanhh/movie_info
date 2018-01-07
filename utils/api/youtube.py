from __future__ import absolute_import
from __future__ import print_function

import requests

__key__ = 'AIzaSyDQFR_Dg84Tl4w9SrwbZL0j30K9Ee3bQBI'

class URL:
    def __init__(self):
        self.get = 'https://www.googleapis.com/youtube/v3/videos?part=statistics&key={key}&id={id}'
        self.search = 'https://www.googleapis.com/youtube/v3/search?part=id&type=video&q={query}&key={key}'

class Youtube:
    def __init__(self):
        self.url = URL()

    def get(self, **kwargs):
        response = requests.request('GET', self.url.get.format(
            key = __key__,
            id = ',+'.join(kwargs['id'])
        ))
        return response.json()

    def search(self, **kwargs):
        response = requests.request('GET', self.url.search.format(
            query = kwargs['query'],
            key = __key__
        ))
        return response.json()
