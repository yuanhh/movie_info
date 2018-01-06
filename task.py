import os
import sys
import json
import requests

from urllib.request import urlopen, HTTPError, URLError
from zipfile import ZipFile

from utils.movie import movie

def download_file(url, movieName):
    # Open the url
    try:
        f = urlopen(url)
        #print("downloading ", url)

        with open('{}.zip'.format(movieName), "wb") as df:
            df.write(f.read())

    #handle errors
    except HTTPError as err:
        print("HTTP Error:", err.code, url)
    except URLError as err:
        print("URL Error:", err.reason, url)

def unzip(movieName):

    os.mkdir(movieName)

    with ZipFile('{}.zip'.format(movieName), 'r') as zf:
        zf.extractall(movieName)

def main():

    mlist = set()
    mlist.update(movie.top(begin = 201501, end = 201513))
    mlist.update(movie.top(begin = 201601, end = 201613))
    mlist.update(movie.top(begin = 201701, end = 201712))

    for mv in list(mlist):
        m = movie.search(query = mv)
        # info = movie.get(imdb_id = m)
        # print(info)
        l = movie.link(query = mv, sublanid = 'zht', imdbid = m)
        if l is not None:
            download_file(l, mv)
            unzip(mv)

if __name__ == '__main__':
    main()
