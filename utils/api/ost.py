from __future__ import absolute_import
from __future__ import print_function

from pythonopensubtitles.opensubtitles import OpenSubtitles

class OST:
    def __init__(self):
        self.api = OpenSubtitles()
        self.api.login("doctest", 'doctest')

    def find_max_dl_count(self, **kwargs):
        target = 0
        for i, e in enumerate(kwargs['data']):
            if int(e['IDMovieImdb']) == int(kwargs['imdb_id'].strip('t')) and \
                e['SubFormat'] == 'srt':
                if int(kwargs['data'][target]['SubDownloadsCnt']) < \
                    int(e['SubDownloadsCnt']):
                    target = i

        return target

    def link(self, **kwargs):
        data = self.api.search_subtitles([{'query':kwargs['query'],
            'sublanguageid':kwargs['sublanid']}])
        target = self.find_max_dl_count(data = data, imdb_id = kwargs['imdb_id'])

        if len(data) == 0:
            return None

        return data[target]['ZipDownloadLink']
