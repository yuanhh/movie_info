import os
import sys
import json
import requests

from utils.movie import movie

def main():
    m = movie.search(query = 'super8')
    print(m)

if __name__ == '__main__':
    main()
