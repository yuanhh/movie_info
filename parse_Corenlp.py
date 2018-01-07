
# coding: utf-8

# In[2]:


import os
from os import listdir
from os.path import isfile, join
from opencc import OpenCC
import json

# nlp 
from pycorenlp import StanfordCoreNLP
import sys

import concurrent.futures

__ip__ = '140.113.24.241'
__port__ = '9000'
__path__ = os.path.dirname(os.path.abspath(__file__))
nlp = StanfordCoreNLP('http://{ip}:{port}'.format(ip = __ip__, port = __port__))

# do parse
# def do_nlp(obj):
#     return nlp.annotate(obj, properties = {
#         'annotators': 'tokenize,ssplit,pos,depparse,parse',
#         'outputFormat': 'json'
#     })

def do_nlp(obj):
    
    print('sub: ' + obj['sub'])
    
    text = nlp.annotate(transfer2s(obj['sub']), properties = {
        'annotators': 'tokenize,ssplit,pos,depparse,parse',
        'outputFormat': 'json'
    })
    with open('data/%s/%s.json' % (obj['imdb'], str(obj['index'])), 'w') as file:
        json.dump(text, file)
    
# transfer traditional chinese to simplified chinese
def transfer2s(ori_str):
    openCC = OpenCC('t2s')  # convert from Simplified Chinese to Traditional Chinese
    return openCC.convert(ori_str)


# parse mv one by one
def main():
    
    imdb = sys.argv[1]
    subs = sys.argv[2]
    
    tmp = {
        'imdb_id': '',
        'encode': '',
        'type': '',
        'title': '',
        'sub': subs,
        'parsed_sub': []
    }
    
    
            
    sub_i = []
    for index, sub in enumerate(subs):
        sub_i.append({
            'imdb': imdb,
            'index': index,
            'sub': sub
        })

    os.makedirs('%s/data/%s' % (__path__, imdb))

    with concurrent.futures.ThreadPoolExecutor(max_workers = 16) as executor:
        futures = executor.map(do_nlp, sub_i, )
        
    json_list = [f for f in os.listdir('data/%s/' % (imdb))]
    
    tmp['parsed_sub'] = [0] * len(json_list)
    
    for f in json_list:
        with open('%s/data/%s/%s' % (__path__, imdb, f), 'r') as fp:
            i = int(f[:f.find('.')])
            tmp['parsed_sub'][i] = json.load(fp)

    with open('data/{}.imdb'.format(imdb), 'w') as out_p:
        json.dump(tmp, out_p)

if __name__ == '__main__':
    main()

