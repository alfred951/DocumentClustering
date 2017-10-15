#!/usr/bin/python

import sys
import time
from DocumentManager import DocumentManager
import Cluster
from os import listdir
from os.path import join, isfile
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.size

if rank == 0:

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

    print "Starting parallel clustering...", '\n'

    files = [f for f in listdir(path) if isfile(join(path, f))]
    files.sort()

    print len(files)
    divided_files = [[] for i in range(size)]
    division_size = int(len(files)/size)
    extra_files = len(files) % size
    print extra_files
    for i in range(len(divided_files)):
        divided_files[i] = files[i*division_size:(i+1)*division_size]
        print len(divided_files[i])
        print divided_files[i]
    print
    print
    if extra_files != 0:
        for i in range(extra_files):
            divided_files[i].append(files[(division_size*size)+i])
            print len(divided_files[i])
            print divided_files[i]

# print "Loading Documents..."
# document_manager = DocumentManager(path)
#
# print "\nTime taken:", time.time() - initial_time, "s"
# print "\nReducing documents..."
#
# initial_time = time.time()
# document_manager.count_words()
#
# print "\nTime taken:", time.time() - initial_time, "s"
# print "\nVectorizing documents..."
#
# initial_time = time.time()
# document_manager.vectorize_documents()
# documents = document_manager.get_documents()
# terms = document_manager.get_terms()
#
# print "\nTime taken:", time.time() - initial_time, "s"
# print "\nStarting K-means Algorithm...\n"
#
# initial_time = time.time()
# centers, clusters, cluster_names = Cluster.find_centers(terms, documents, 4)
#
# print "\nTime taken:", time.time() - initial_time, "s"
#
# i = 0
# for cluster in clusters:
#     print
#     print "Documents in cluster", cluster_names[i], '\n'
#     for document in cluster:
#         print document.get_name()
#     i = i+1
