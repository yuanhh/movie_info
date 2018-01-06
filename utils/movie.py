from __future__ import absolute_import
from __future__ import print_function

import os
import sys
import json
import requests

from utils.api.tmdb import TMDB
from utils.api.douban import Douban
from utils.api.youtube import Youtube

class API:
    def __init__(self):
        self.tmdb = TMDB()
        self.douban = Douban()
        self.youtube = Youtube()

class Movie:
    def __init__(self):
        self.api = API()

    def get(self, **kwargs):
        return {
            'tmdb': self.api.tmdb.find(imdb_id = kwargs['imdb_id']),
            'douban': self.api.douban.get(imdb_id = kwargs['imdb_id'])
        }

    def search(self, **kwargs):
        return {
            'tmdb': self.api.tmdb.search(query = kwargs['query'])
        }

    def trend(self, **kwargs):
        pass

# rename
movie = Movie()
