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

    movieList = getMovieList()

    out_f = open('{}/data/{}'.format(__path__, 'movie_info.txt'), 'w')
    for mv in list(movieList):
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

# Step 1:
#   Get the movie list from file(movie_list.txt)
#   Download from google trend it file not found
def getMovieList():
    movieList = []

    movieListFileName = '{}/data/{}'.format(__path__, 'movie_list.txt')
    try:
        with open(movieListFileName, 'r') as f:
            movieList = json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        print("Let's download movie list.".format(movieListFileName))
        movieList = set()
        movieList.update(movie.top(begin = 201501, end = 201513))
        movieList.update(movie.top(begin = 201601, end = 201613))
        movieList.update(movie.top(begin = 201701, end = 201712))
        movieList = list(movieList)
        with open(movieListFileName, 'w+') as f:
            json.dump(movieList, f)
    return movieList

if __name__ == '__main__':
    main()
