#!/usr/bin/python

import sys
import time
from DocumentManager import DocumentManager
import Comparator
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

document_manager = DocumentManager(path)
document_manager.count_words()
document_manager.vectorize_documents()
documents = document_manager.get_documents()
filenames = document_manager.get_filenames()

print "document 0:", filenames[0]
print "document 1:", filenames[1]
print "--------------------------------------------"
print "Euclidean distance between 0 and 1:", Comparator.calculate_euclidean_distance(documents[0], documents[1])
print "Cosine distance between 0 and 1:", Comparator.calculate_cosine_distance(documents[0], documents[1])
print "Jaccard distance between 0 and 1:", Comparator.calculate_jaccard_distance(documents[0], documents[1])
print '\n'
print "document 3:", filenames[3]
print "document 7:", filenames[7]
print "--------------------------------------------"
print "Euclidean distance between 3 and 7:", Comparator.calculate_euclidean_distance(documents[3], documents[7])
print "Cosine distance between 3 and 7:", Comparator.calculate_cosine_distance(documents[3], documents[7])
print "Jaccard distance between 3 and 7:", Comparator.calculate_jaccard_distance(documents[3], documents[7])
print '\n'
print "document 0:", filenames[0]
print "document 8:", filenames[8]
print "--------------------------------------------"
print "Euclidean distance between 0 and 8:", Comparator.calculate_euclidean_distance(documents[0], documents[8])
print "Cosine distance between 0 and 8:", Comparator.calculate_cosine_distance(documents[0], documents[8])
print "Jaccard distance between 0 and 8:", Comparator.calculate_jaccard_distance(documents[0], documents[8])
print '\n'
print "document 4:", filenames[4]
print "document 4:", filenames[4]
print "--------------------------------------------"
print "Euclidean distance between 4 and 4:", Comparator.calculate_euclidean_distance(documents[4], documents[4])
print "Cosine distance between 4 and 4:", Comparator.calculate_cosine_distance(documents[4], documents[4])
print "Jaccard distance between 4 and 4:", Comparator.calculate_jaccard_distance(documents[4], documents[4])
print '\n'

print "Starting K-means Algorithm..."

centers, clusters = Cluster.find_centers(documents, 2)
for i in clusters:
    print i, "cluster contents", clusters

print "\nTime taken:", time.time() - initial_time, "s"
