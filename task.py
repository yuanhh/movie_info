import os
import sys
import json
import requests

from urllib.request import urlretrieve, HTTPError, URLError
from zipfile import ZipFile

from utils.movie import movie

__path__ = os.path.dirname(os.path.abspath(__file__))

def download_file(url, movieName):
    # Open the url
    try:
        f = urlretrieve(url, '{}/data/{}.zip'.format(__path__, movieName))
        #print("downloading ", url)
        return True

    #handle errors
    except HTTPError as err:
        print("HTTP Error:", err.code, url)
        return False
    except URLError as err:
        print("URL Error:", err.reason, url)
        return False

def unzip(movieName):

    fileList = os.listdir('{}/data'.format(__path__))
    if movieName in fileList:
        return

    os.mkdir('{}/data/{}'.format(__path__, movieName))
    with ZipFile('{}/data/{}.zip'.format(__path__, movieName), 'r') as zf:
        zf.extractall('{}/data/{}'.format(__path__, movieName))

def main():

    mlist = set()
    mlist.update(movie.top(begin = 201501, end = 201513))
    mlist.update(movie.top(begin = 201601, end = 201613))
    mlist.update(movie.top(begin = 201701, end = 201712))

    out_f = open('{}/data/{}'.format(__path__, 'movie_info.txt'), 'w')
    for mv in list(mlist):
        m = movie.search(query = mv)
        info = movie.get(imdb_id = m)
        l = movie.link(query = mv, sublanid = 'zht', imdbid = m)

        info['title']['en'] = mv
        info['zipUrl'] = l

        if l is not None:
            if download_file(l, mv):
                unzip(mv)

        out_f.write(json.dumps(info, indent = 4))

    out_f.close()

if __name__ == '__main__':
    main()
