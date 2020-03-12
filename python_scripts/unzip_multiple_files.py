'''
This script will unzip multiple zip files places at different sub-directories of same parent directory.
'''

import os
import zipfile
import sys

def unzip_files():
    DIR=sys.argv[1]

    for (root, dir, files) in os.walk(DIR):
        for fname in files:
            if('.zip' in fname):
                zip_file = os.path.join(root, fname)
                print("Extracting ", zip_file, '... Please wait...')
                zipref = zipfile.ZipFile(zip_file, 'r')
                zipref.extractall(root)
                zipref.close()
                print(zip_file, 'is extracted Successfully!')


if __name__ == "__main__":
    unzip_files()
