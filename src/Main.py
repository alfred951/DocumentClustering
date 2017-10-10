#!/usr/bin/python

import sys

import time

from DocumentManager import DocumentManager

initial_time = time.time()
path = "../assets/Gutenberg/txt/"

if len(sys.argv) == 1:
    print "\nSetting default path:", path

if len(sys.argv) == 2:
    if sys.argv[1] == "-h":
        print ("Compares and clusters documents, "
               "[-p path] sets the path to a specified location")
    sys.exit()

if len(sys.argv) == 3:
    if sys.argv[1] == "-p":
        path = sys.argv[2]
        print "The path is:", path, '\n'

print "Starting serial clustering...", '\n'

document_manager = DocumentManager(path)
document_manager.count_words()
document_manager.vectorize_documents()

print "Time taken:", time.time() - initial_time, "s"
