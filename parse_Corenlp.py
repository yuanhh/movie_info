# -*- coding: utf-8 -*-  

import os
import sys
import re
import pysrt
from os import listdir
from os.path import isfile, join
from opencc import OpenCC
import json

from utils.movie import movie

# nlp 
from pycorenlp import StanfordCoreNLP

import concurrent.futures

__ip__ = '140.113.24.241'
__port__ = '9000'
__path__ = os.path.dirname(os.path.abspath(__file__))
nlp = StanfordCoreNLP('http://{ip}:{port}'.format(ip = __ip__, port = __port__))

def do_nlp(obj):

    print("doing: " + obj['sub'])
    text = nlp.annotate(transfer2s(obj['sub']), properties = {
        'annotators': 'tokenize,ssplit,pos,depparse,parse',
        'outputFormat': 'json'
    })
    with open('result/%s/%s.json' % (obj['imdb'], str(obj['index'])), 'w') as file:
        json.dump(text, file)
    
# transfer traditional chinese to simplified chinese
def transfer2s(ori_str):
    openCC = OpenCC('t2s')  # convert from Simplified Chinese to Traditional Chinese
    return openCC.convert(ori_str)

def read_srt(f):
    if f.endswith('.srt'):
        try:
            return pysrt.open('{}/srts/{}'.format(__path__, f))
        except UnicodeDecodeError:
            return

# parse mv one by one
def main():
    
    imdb_list = os.listdir('{}/srts/'.format(__path__))
    for imdb_f in imdb_list:
        imdb, ext =  os.path.splitext(imdb_f)
        subs = read_srt(imdb_f)
        if subs is None:
            continue

        print(imdb)
        sub_i = []
        sub_l = []
        for index, sub in enumerate(subs):
            raw_sub = re.sub('{.*}', '', sub.text).strip('-')
            sub_l.append(raw_sub)
            sub_i.append({
                'imdb': imdb,
                'index': index,
                'sub': raw_sub
            })
    
        tmp = {
            'imdb_id': '',
            'encode': '',
            'type': '',
            'title': '',
            'sub': sub_l,
            'parsed_sub': []
        }
                
        os.makedirs('%s/result/%s' % (__path__, imdb))
    
        with concurrent.futures.ThreadPoolExecutor(max_workers = 16) as executor:
            futures = executor.map(do_nlp, sub_i, )
            
        json_list = [f for f in os.listdir('result/%s/' % (imdb))]
        
        tmp['parsed_sub'] = list()
        
        for f in json_list:
            with open('%s/result/%s/%s' % (__path__, imdb, f), 'r') as fp:
                tmp['parsed_sub'].append(json.load(fp))
    
        with open('result/{}.imdb'.format(imdb), 'w') as out_p:
            json.dump(tmp, out_p)

if __name__ == '__main__':
    main()
