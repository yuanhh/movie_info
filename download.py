import os
import json
import requests
import concurrent.futures

def get(movie):
    print(movie)
    r = requests.request('GET', movie['link'])
    if r.status_code == 200:
        with open('srts/%s.zip' % movie['imdb_id'], 'wb') as outfile:
            outfile.write(r.content)

def main():
    srts = os.listdir('srts')
    srts = [srt[:srt.find('.')] for srt in srts]

    dls = os.listdir('dls')
    dls = [dl[:dl.find('.')] for dl in dls]
    dls = [dl for dl in dls if dl not in srts]

    movies = []

    for dl in dls:
        with open('dls/%s.dl' % dl, 'r') as infile:
            movies.append(json.load(infile))

    with concurrent.futures.ThreadPoolExecutor(max_workers = 2) as executor:
        futures = executor.map(get, movies, )

if __name__ == '__main__':
    main()
