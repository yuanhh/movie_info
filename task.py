import os
import sys
import json
import requests

from utils.movie import movie
from utils.subtitle import subtitle

__path__ = os.path.dirname(os.path.abspath(__file__))

def mkdir(dir_name):
    try:
        os.mkdir(dir_name)
    except:
        pass

def get_dls(m, info):
    q = info.get('title')
    imdb = info.get('imdb_id')
    if q is None or imdb is None:
        return

    dl, enc = subtitle.link(query = q, imdb_id = imdb, sublanid = 'zht')
    if dl is not None:
        json.dumps(info)
        with open('dls/%s.dl' % info['imdb_id'], 'w') as outfile:
            json.dump({
                'imdb_id': info['imdb_id'], 
                'link': dl, 
                'encoding': enc}
                , outfile)

def main():
    mkdir('dls')

    tasks = os.listdir('tasks')
    tasks = [task[:task.find('.')] for task in tasks]

    dls = os.listdir('dls')
    dls = [dl[:dl.find('.')] for dl in dls]

    movies = [x for x in tasks if x not in dls]

    for i, m in enumerate(movies):
        with open('tasks/%s.task' % m, 'r') as f:
            movie_info = json.load(f)

        if movie_info is None:
            continue

        print(str(i) + '\t' + json.dumps(movie_info))
        get_dls(m, movie_info)

if __name__ == '__main__':
    main()
