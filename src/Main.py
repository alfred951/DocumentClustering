#!/usr/bin/python

import sys
import time
from DocumentManager import DocumentManager
import Cluster

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

print "Loading Documents..."
document_manager = DocumentManager(path)

print "\nTime taken:", time.time() - initial_time, "s"
print "\nReducing documents..."

initial_time = time.time()
document_manager.count_words()

print "\nTime taken:", time.time() - initial_time, "s"
print "\nVectorizing documents..."

initial_time = time.time()
document_manager.vectorize_documents()
documents = document_manager.get_documents()

print "\nTime taken:", time.time() - initial_time, "s"
print "\nStarting K-means Algorithm..."

initial_time = time.time()
centers, clusters = Cluster.find_centers(documents, 4)

print "\nTime taken:", time.time() - initial_time, "s"

i = 1
for cluster in clusters:
    print
    print "Documents in cluster", i, '\n'
    for document in cluster:
        print document.get_name()
    i = i+1
