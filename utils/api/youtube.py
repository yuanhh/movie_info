from __future__ import absolute_import
from __future__ import print_function

import pafy

class Youtube:
    def __init__(self):
        pass

    def get(self, **kwargs):
        video = pafy.new(kwargs['url'])

        return video
