import os

from utils.movie import movie

__path__ = os.path.abspath(os.path.dirname(__file__)) + '/srts'

def main():
    files = os.listdir('srts')

    for file in files:
        name = file[:file.find('(') - 1]
        year = file[file.find('(') + 1: file.find(')')]

        result = movie.search(query = name.replace('.', ' '))

        if result == None:
            print('Not found: %s' % file)
            continue

        if year not in result['release_date']:
            print('Not found: %s' % file)
            continue

        src = '%s/%s' % (__path__, file)
        dst = '%s/%s.zip' % (__path__, result['imdb_id'])

        print(src, dst)
        os.rename(src, dst)

if __name__ == '__main__':
    main()
