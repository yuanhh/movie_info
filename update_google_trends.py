import os
import sys
import json
import requests

from utils.movie import movie
from utils.subtitle import subtitle

__path__ = os.path.dirname(os.path.abspath(__file__))

def getMovieList():
    movieList = []

    movieListFileName = '{}/{}'.format(__path__, 'movie_list.txt')
    try:
        with open(movieListFileName, 'r') as f:
            movieList = json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        print("Let's download movie list.".format(movieListFileName))
        movieList = set()
        movieList.update(movie.top(begin = 200801, end = 200813))
        movieList.update(movie.top(begin = 200901, end = 200913))
        movieList.update(movie.top(begin = 201001, end = 201013))
        movieList.update(movie.top(begin = 201101, end = 201113))
        movieList.update(movie.top(begin = 201201, end = 201213))
        movieList.update(movie.top(begin = 201301, end = 201313))
        movieList.update(movie.top(begin = 201401, end = 201413))
        movieList.update(movie.top(begin = 201501, end = 201513))
        movieList.update(movie.top(begin = 201601, end = 201613))
        movieList.update(movie.top(begin = 201701, end = 201712))
        movieList = list(movieList)
        with open(movieListFileName, 'w+') as f:
            json.dump(movieList, f)
    return movieList

def mkdir(dir_name):
    try:
        os.mkdir(dir_name)
    except:
        pass

def get_imdb_id(mv_name_list):
    for m in mv_name_list:
        print(m)
        res = movie.search(query = m)

        with open('tasks/%s.task' % res['imdb_id'], 'w+') as f:
            json.dump({'imdb_id': res['imdb_id'], 'title': m}, f)

def main():

    # get movielist from google trends top charts
    movieList = getMovieList()

    mkdir('tasks')

    get_imdb_id(movieList)

if __name__ == '__main__':
    main()
