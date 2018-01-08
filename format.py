import os
import fnmatch
import requests

def main():
    folders = os.listdir('srts')

    for folder in folders:
        files = [file for file in os.listdir('srts/%s' % folder) if fnmatch.fnmatch(file, '*.srt')]

        if len(files) != 1:
            print(folder)
            continue

        src = 'srts/%s/%s' % (folder, files[0])
        dst = 'srts/%s.srt' % folder

        print(src, dst)

        os.rename(src, dst)

if __name__ == '__main__':
    main()
