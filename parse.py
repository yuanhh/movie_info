
# coding: utf-8

# In[2]:


import os
from os import listdir
from os.path import isfile, join
from opencc import OpenCC
import pysrt
import json

# nlp 
from pycorenlp import StanfordCoreNLP
import sys

# jieba
import jieba
import jieba.posseg
import jieba.analyse


# In[3]:


# transfer traditional chinese to simplified chinese
def transfer2s(ori_str):
    openCC = OpenCC('t2s')  # convert from Simplified Chinese to Traditional Chinese
    return openCC.convert(ori_str)


# In[4]:


# parsed by jieba
def parse(s):
    tmp = transfer2s(s)
    words = jieba.posseg.cut(s)
    tmp = []
    for word, flag in words:
        tmp.append([word, flag])
    return tmp


# In[5]:


# parse mv one by one
def main():
    encode = 'UTF-8'
    with open('data/mv_list.json', 'r') as in_p:
        mvs = json.load(in_p)
        
    for imdb, mv in mvs.items():
        print(imdb + '=====')
        if 'subs' in mvs[imdb]:
            continue
        mvs[imdb]['subs'] = []
        if mv['srt_name'] != '' and mv['srt_name'] != 'unknown srt name':
            if mv['srt_info'][2] != 0:
                subs = pysrt.open('data/srt/{}'.format(mv['srt_name']), encoding = mv['srt_info'][2])
            else:
                subs = pysrt.open('data/srt/{}'.format(mv['srt_name']), encoding = encode)

            for index, sub in enumerate(subs):
                mvs[imdb]['subs'].append([sub.text, parse(sub.text)])
    with open('data/mv_subs_parsed.json', 'w') as out_p:
        json.dump(mvs, out_p)


# In[ ]:


if __name__ == '__main__':
    main()

