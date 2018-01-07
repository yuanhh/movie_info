import os
import sys
import math
import pysrt
import json
import io
import jieba

__path__ = os.path.dirname(os.path.abspath(__file__))

def tfidf(tf, df, docCount):
    for movie in tf:
        with open('{}/data/{}/{}'.format(__path__, movie, 'tfidf.txt'),
                'w') as out_f:
            for seg in df:
                val = tf[movie].get(seg)
                if val is None:
                    val = 0
                else:
                    val = val * math.log2(docCount / df[seg])
                out_f.write(seg + '\t' + str(val) + '\n')

def termFreq(tf, seg_list, movie):
    for seg in seg_list:
        freq = tf[movie].get(seg)
        if freq is None:
            tf[movie][seg] = 1
        else:
            tf[movie][seg] += 1

def docFreq(tf, df, movie):
    for seg in tf[movie]:
        freq = df.get(seg)
        if freq is None:
            df[seg] = 1
        else:
            df[seg] += 1

def extract_movie_line(movie):
    contents = os.listdir('{}/data/{}'.format(__path__, movie))
    for f in contents:
        if f.endswith('.srt'):
            try:
                return pysrt.open('{}/data/{}/{}'.format(__path__, movie, f))
            except UnicodeDecodeError:
                continue

def main():
    docCount = 0
    df = dict()
    tf = dict()
    movieList = os.listdir('{}/data/'.format(__path__))
    for movie in movieList:
        tf[movie] = dict()
        subs = extract_movie_line(movie)
        if subs is None:
            continue
        for sub in subs:
            seg_list = jieba.cut(sub.text)
            termFreq(tf, seg_list, movie)

        docCount = docCount + 1
        docFreq(tf, df, movie)

    tfidf(tf, df, docCount)

if __name__ == '__main__':
    main()
