#!/usr/bin/python

import sys
from DocumentManager import DocumentManager

path = "../assets/Gutenberg/txt/"

if len(sys.argv) == 1:
    print "Setting default path:", path

if len(sys.argv) == 2:
    if sys.argv[1] == "-h":
        print ("Compares and clusters documents, "
               "[-p path] sets the path to a specified location")
    sys.exit()

if len(sys.argv) == 3:
    if sys.argv[1] == "-p":
        path = sys.argv[2]
        print "The path is:", path

Doc = DocumentManager(path)
Doc.get_filenames()
Doc.generate_dictionary()
