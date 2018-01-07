from __future__ import absolute_import
from __future__ import print_function

from utils.api.ost import OST

class API:
    def __init__(self):
        self.ost = OST()

class Subtitle:
    def __init__(self):
        self.api = API()

    def link(self, **kwargs):
        return self.api.ost.link(query = kwargs['query'],
            sublanid = kwargs['sublanid'], imdb_id = kwargs['imdbid'])

# rename
subtitle = Subtitle()
