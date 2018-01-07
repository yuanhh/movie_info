from __future__ import absolute_import
from __future__ import print_function

import os
import sys
import json
import requests

from utils.api.tmdb import TMDB
from utils.api.gtrends import Gtrend
from utils.api.douban import Douban
from utils.api.youtube import Youtube

class API:
    def __init__(self):
        self.tmdb = TMDB()
        self.douban = Douban()
        self.youtube = Youtube()
        self.gtrend = Gtrend()

class Movie:
    def __init__(self):
        self.api = API()

    def get(self, **kwargs):
        return {
            'tmdb': self.api.tmdb.find(imdb_id = kwargs['imdb_id']),
            'douban': self.api.douban.get(imdb_id = kwargs['imdb_id'])
        }

    def search(self, **kwargs):
        tmdb = self.api.tmdb.search(query = kwargs['query'])
        imdb = self.api.tmdb.get(movie_id = tmdb['id'])

        return imdb

    def trend(self, **kwargs):
        result = self.api.youtube.search(query = kwargs['query'] + ' ' + 'trailer')
        result = self.api.youtube.get(id = [x['id']['videoId'] for x in result['items']])

        return {
            'tmdb': self.search(query = kwargs['query'])['popularity'],
            'youtube': max([x['statistics']['viewCount'] for x in result['items']])
        }

    def top(self, **kwargs):
        return self.api.gtrend.top(begin = kwargs['begin'], end = kwargs['end'])

# rename
movie = Movie()
