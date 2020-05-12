#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3
""" This program reads in a file, and outputs the number of:
lines
words
chararcter, including spaces and special characters, but not including the newline

"""
import os


import sys
import re

file_path = sys.argv[1]

lines, words, chars = 0,0,0

if os.path.exists(file_path):                
    try:
        with open(file_path) as fp:
            for line in fp:
                line = line.rstrip()
                if line != '':
                    lines = lines + 1
                    words = words + len(line.split())
                    chars = chars + len(line)
        print ("{} lines, {} words, {} chars".format(lines, words, chars))
    except Exception as e :
        print("Error occurred", "aborting")
else:
    print("File does not exist, aborting")
    