import os
import sys
import math
import json
import io

__path__ = os.path.dirname(os.path.abspath(__file__))

def tfidf(tf, df, docCount):
    for imdb_id in tf:
        with open('result/{}.tfidf'.format(imdb_id), 'w') as out_f:
            for tok in tf[imdb_id]:
                val = tf[imdb_id][tok] * math.log2(docCount / df[tok])
                print(tok + '\t' + str(val) + '\n')
                out_f.write(tok + '\t' + str(val) + '\n')

def termFreq(tf, tokens, imdb_id):
    for tok in tokens:
        freq = tf[imdb_id].get(tok)
        if freq is None:
            tf[imdb_id][tok] = 1
        else:
            tf[imdb_id][tok] += 1

def docFreq(tf, df, imdb_id):
    for tok in tf[imdb_id]:
        freq = df.get(tok)
        if freq is None:
            df[tok] = 1
        else:
            df[tok] += 1

def get_token(subs):
    tokens = list()
    for i, sub in enumerate(subs['sentences']):
        for j, token in enumerate(sub['tokens']):
            tokens.append(token['word'])

    return tokens

def main():
    # initialize
    docCount = 0
    df = dict()
    tf = dict()

    imdb_list = os.listdir('{}/result/'.format(__path__))
    for imdb_f in imdb_list:
        if not imdb_f.endswith('.imdb'):
            continue

        imdb_id, ext =  os.path.splitext(imdb_f)
        tf[imdb_id] = dict()

        with open('result/{}'.format(imdb_f), 'r') as info_p:
            data = json.load(info_p)
    
        for i, subs in enumerate(data['parsed_sub']):
            if type(subs) is not dict:
                continue

            tokens = get_token(subs)
            if tokens is None:
                return

            termFreq(tf, tokens, imdb_id)

        docCount = docCount + 1
        docFreq(tf, df, imdb_id)

    tfidf(tf, df, docCount)

if __name__ == '__main__':
    main()
