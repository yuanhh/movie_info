import os
import sys
import json
import fnmatch
import requests
import concurrent.futures

from utils.movie import movie
from utils.subtitle import subtitle

__key__ = '368858ba0976e216625527ac96a9f52d'
__path__ = os.path.dirname(os.path.abspath(__file__))

def run(index):
    r = requests.request('GET', 'https://api.themoviedb.org/3/movie/popular', data = {
        'api_key': __key__,
        'language': 'en-US',
        'page': index
    }).json()

    with open('movie_list_%04d.json' % index, 'w') as outfile:
        json.dump(r['results'], outfile)

def tmdb_to_imdb(x):
    r = movie.api.tmdb.get(movie_id = x['movie_id'])

    with open('%s.imdb' % r['imdb_id'], 'w') as outfile:
        outfile.write(x['title'])

def get(x, link):
    r = requests.request('GET', link)

    if r.status_code == 200:
        with open('srts/%s.zip' % x['imdb_id'], 'wb') as outfile:
            outfile.write(r.content)
            outfile.close()

def get_link(x):
    print(x)
    link = subtitle.link(query = x['title'], imdb_id = x['imdb_id'], sublanid = 'zht')

    if link == None:
        print('Not found')
        return

    result = {
        'title': x['title'],
        'imdb_id': imdb_id,
    }

    with open('%s' % file, 'w') as outfile:
        json.dump(result, outfile)
        outfile.close()

def main():
    # var
    imdbs = []
    results = []

    '''
    r = requests.request('GET', 'https://api.themoviedb.org/3/movie/popular', data = {
        'api_key': __key__,
        'language': 'en-US',
    })

    total_pages = r.json()['total_pages']

    with concurrent.futures.ThreadPoolExecutor(max_workers = 4) as executor:
        futures = executor.map(run, range(1, total_pages), )

    '''

    '''
    regex = 'movie_list_*.json'
    files = sorted([file for file in os.listdir('.') if fnmatch.fnmatch(file, regex)])

    for file in files:
        print(file)
        with open(file, 'r') as infile:
            try:
                movies = json.load(infile)
            except:
                continue

            for x in movies:
                results.append({'movie_id': x['id'], 'title': x['title']})

    with open('list.json', 'w') as outfile:
        json.dump(results, outfile)
    '''

    '''
    with open('list.json', 'r') as infile:
        data = infile.read()
        movies = json.loads(data)

    with concurrent.futures.ThreadPoolExecutor(max_workers = 8) as executor:
        futures = executor.map(tmdb_to_imdb, movies, )
    '''



if __name__ == '__main__':
    main()
