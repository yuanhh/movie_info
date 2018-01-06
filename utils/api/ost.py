from __future__ import absolute_import
from __future__ import print_function

from pythonopensubtitles.opensubtitles import OpenSubtitles

class OST:
    def __init__(self):
        self.api = OpenSubtitles()

    def find_max_dl_count(self, data, imdbid):
        target = 0
        for i, e in enumerate(data):
            if int(e['IDMovieImdb']) == int(imdbid.strip('t')) and \
                e['SubFormat'] == 'srt':
                if int(data[target]['SubDownloadsCnt']) < \
                    int(e['SubDownloadsCnt']):
                    target = i

        print(target)
        return target

    def link(self, **kwargs):
        token = self.api.login("doctest", 'doctest')
        data = self.api.search_subtitles([{'query':kwargs['query'],
            'sublanguageid':kwargs['sublanid']}])
        target = self.find_max_dl_count(data, kwargs['imdbid'])

        if len(data) == 0:
            return None

        return data[target]['ZipDownloadLink']
