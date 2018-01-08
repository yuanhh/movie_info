import os
import sys
import time
import fnmatch
import concurrent.futures

def feed(raw):
    os.system('python3 corenlp.py %s' % raw)

def main():
    raws = [file for file in os.listdir('srts') if fnmatch.fnmatch(file, '*.srt')]
    raws = [raw[:raw.find('.')] for raw in raws]

    parseds = [file for file in os.listdir('data') if fnmatch.fnmatch(file, '*.imdb')]
    parseds = [parsed[:parsed.find('.')] for parsed in parseds]

    raws = [raw for raw in raws if raw not in parseds]

    print(len(raws))

    with concurrent.futures.ThreadPoolExecutor(max_workers = 4) as executor:
        futures = executor.map(feed, raws, )

if __name__ == '__main__':
    main()
