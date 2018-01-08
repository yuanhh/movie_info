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
    sub = subtitle.link(query = x['title'], imdb_id = x['imdb_id'], sublanid = 'zht')
    if sub != None:
        print('O\t%s' % x)
        with open('dls/%s.dl' % x['imdb_id'], 'w') as outfile:
            json.dump({
                'imdb_id': x['imdb_id'],
                'link': sub['ZipDownloadLink'],
                'encoding': sub['SubEncoding']
            }, outfile)
    else:
        print('X\t%s' % x)
        os.remove('tasks/%s.task' % x['imdb_id'])

def main():
    # var
    tasks = []
    files = [f[:f.find('.')] for f in os.listdir('tasks') if fnmatch.fnmatch(f, '*.task')]
    dls = [f[:f.find('.')] for f in os.listdir('dls') if fnmatch.fnmatch(f, '*.dl')]

    files = sorted([f for f in files if f not in dls])

    print(len(files))

    for file in files:
        with open('tasks/%s.task' % file, 'r') as infile:
            tasks.append(json.load(infile))

    # for task in tasks:
    #     with open('tasks/%s.task' % task, 'r') as infile:
    #         x = json.load(infile)
    #     run(x)
    #     break

    with concurrent.futures.ThreadPoolExecutor(max_workers = 3) as executor:
        futures = executor.map(run, tasks, )


if __name__ == '__main__':
    main()
