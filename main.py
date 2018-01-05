import os
import sys
import json
import requests

from utils.movie import movie

def main():
    m = movie.search(query = 'frozen')
    print(m)
    info = movie.get(imdb_id = m)
    print(info)

if __name__ == '__main__':
    main()
