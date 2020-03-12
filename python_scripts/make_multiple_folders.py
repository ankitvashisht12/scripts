'''
This command will make multiple folders inside the given path
'''

import os
import sys
import argparse

desp = "Arguments description"

# Initialize parser
parser = argparse.ArgumentParser(description=desp)

# Adding optional argument
parser.add_argument("-d", "--directory", help="Parent directory path")
parser.add_argument("-n", "--number", help="Number of folders")
parser.add_argument("-p", '--phrase', help="Initial phrase for folder name")
parser.add_argument("-s", '--start', help="number to start with (default is 1)")
parser.add_argument("-v", "--verbose", help="Print output. Default is 0")


args = parser.parse_args()

DIR = args.directory
NUM = int(args.number)
PHRASE = args.phrase
if args.verbose:
    VERBOSE = int(args.verbose)
else:
    VERBOSE = 0
if(args.start):
    START = int(args.start)
else:
    START = 1

for i in range(NUM):
    file_name = PHRASE+str(i+START)
    temp  = os.system("mkdir %s" % file_name)
    if(VERBOSE):
        print(file_name, "created.")