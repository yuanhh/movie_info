import os

def main():
    srts = [folder for folder in os.listdir('srts')]

    zips = os.listdir('zips')
    zips = [zip[:zip.find('.')] for zip in zips]

    for zip in zips:
        if zip not in srts:
            try:
                os.mkdir('srts/%s' % zip)
            except:
                pass

        command = 'unzip -q -o zips/%s -d srts/%s' % (zip + '.zip', zip)
        print(command)
        os.system(command)

if __name__ == '__main__':
    main()
