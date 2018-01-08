import os
import json

def main():
    with open('imdb.json', 'r') as infile:
        movies = json.load(infile)

    for movie in movies:
        with open('tasks/%s.task' % movie['imdb_id'], 'w') as outfile:
            json.dump(movie, outfile)

if __name__ == '__main__':
    main()
