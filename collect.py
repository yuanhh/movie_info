import os
import sys
import json
import fnmatch
import requests
import concurrent.futures

from utils.subtitle import subtitle

__key__ = '368858ba0976e216625527ac96a9f52d'
__path__ = os.path.dirname(os.path.abspath(__file__))

def run(x):
    x = subtitle.link(query = x['title'], imdb_id = x['imdb_id'], sublanid = 'zht')
    print(x)

    #
    # if x['link'] != None:
    #     with open('dls/%s.dl' % x['imdb_id'], 'w') as outfile:
    #         json.dump(x, outfile)

def main():
    with open('imdb.json', 'r') as infile:
        movies = json.load(infile)

    dls = os.listdir('dls')
    dls = [dl[:dl.find('.')] for dl in dls]

    movies = [x for x in movies if x['imdb_id'] not in dls]

    for x in movies:
        run(x)

    # print(len(movies))
    #
    # with concurrent.futures.ThreadPoolExecutor(max_workers = 2) as executor:
    #     futures = executor.map(run, movies[:1000], )
    #
    # movies = movies[1000:]
    #
    # with open('imdb.json', 'w') as outfile:
    #     json.dump(movies, outfile)

if __name__ == '__main__':
    main()
