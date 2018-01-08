import os
import sys
import json
import pysrt
import concurrent.futures

from opencc import OpenCC
from pycorenlp import StanfordCoreNLP
from utils.movie import movie

__ip__ = '140.113.24.241'
__port__ = '9000'
__path__ = os.path.dirname(os.path.abspath(__file__))

# global
openCC = OpenCC('t2s')
nlp = StanfordCoreNLP('http://{ip}:{port}'.format(ip = __ip__, port = __port__))

def do_nlp(task):
    print(task)
    text = nlp.annotate(openCC.convert(task['sub']), properties = {
        'annotators': 'tokenize,ssplit,pos,depparse,parse',
        'outputFormat': 'json'
    })
    with open('data/%s/%05d.json' % (task['imdb_id'], task['index']), 'w') as outfile:
        json.dump(text, outfile)

def main():
    # var
    imdb_id = sys.argv[1]

    info = movie.get(imdb_id = imdb_id)

    try:
        subs = pysrt.open('srts/%s.srt' % imdb_id, encoding = 'cp950')
    except:
        print('Error: pysrt.open()')
        exit()

    try:
        os.mkdir('data/%s' % imdb_id)
    except:
        pass

    tasks = [{'imdb_id': imdb_id, 'sub': sub.text, 'index': subs.index(sub)} for sub in subs]

    with concurrent.futures.ThreadPoolExecutor(max_workers = 4) as executor:
        futures = executor.map(do_nlp, tasks, )

    results = {
        'imdb_id': imdb_id,
        'encode': 'cp950',
        'type': info['douban']['movie_type'],
        'title': info['douban']['title'],
        'sub': [sub.text for sub in subs],
        'parsed_sub': []
    }

    for file in os.listdir('data/%s/' % imdb_id):
        with open('data/%s/%s' % (imdb_id, file), 'r') as infile:
            data = infile.read()
            results['parsed_sub'].append(data)

    with open('data/%s.imdb' % imdb_id, 'w') as outfile:
        json.dump(results, outfile)

if __name__ == '__main__':
    main()
