import os
import json
import fnmatch

def main():
    imdbs = [file for file in os.listdir('data') if fnmatch.fnmatch(file, '*.imdb')]

    with open('imdb.json', 'r') as infile:
        movies = json.load(infile)

    print(len(movies))

    for imdb in imdbs:
        for movie in movies:
            if imdb[:imdb.find('.')] == movie['imdb_id']:
                del movies[movies.index(movie)]

    with open('imdb.json', 'w') as outfile:
        json.dump(movies, outfile)


if __name__ == '__main__':
    main()
