import os
import sys
import json
import requests

from utils.movie import movie

def main():

    mlist = set()
    mlist.update(movie.top(begin = 201501, end = 201513))
    mlist.update(movie.top(begin = 201601, end = 201613))
    mlist.update(movie.top(begin = 201701, end = 201712))

    for mv in list(mlist):
        m = movie.search(query = mv)
        print(m)
        info = movie.get(imdb_id = m)
        print(info)
        l = movie.link(query = mv, sublanid = 'zht', imdbid = m)
        print(l)

if __name__ == '__main__':
    main()
