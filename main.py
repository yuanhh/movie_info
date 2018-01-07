import os
import sys
import json
import requests

from utils.movie import movie

from utils.api.youtube import Youtube

def main():

    m = movie.search(query = 'super8')
    print(m)
    info = movie.get(imdb_id = m['imdb_id'])
    print(info)

    trend = movie.trend(query = 'super8')
    print(trend)

if __name__ == '__main__':
    main()
