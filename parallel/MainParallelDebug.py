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
initial_time = time.time()
path = "../assets/Gutenberg/txt/"

if rank == 0:

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
    print "Found", len(files), "files"
    divided_files = [[] for i in range(size - 1)]
    division_size = int(len(files) / (size - 1))
    extra_files = len(files) % (size - 1)
    for i in range(len(divided_files)):
        divided_files[i] = files[i * division_size:(i + 1) * division_size]
    for i in range(extra_files):
        divided_files[i].append(files[(division_size * (size - 1)) + i])
    for i in range(1, size):
        comm.send(divided_files[i - 1], dest=i)

if rank != 0:
    files = comm.recv(source=0)

    print "\nRank", rank, "Loading Documents..."
    document_manager = DocumentManager(path, files)

    print "\nRank", rank, "Time taken:", time.time() - initial_time, "s"
    print "\nRank", rank, "Reducing documents..."

    initial_time = time.time()
    document_manager.count_words()

    print "\nRank", rank, "Time taken:", time.time() - initial_time, "s"
    print "\nRank", rank, "Sending terms to master..."

    terms = document_manager.get_terms()
    comm.send(terms, dest=0)

if rank == 0:
    print "\nRank", rank, "Recollecting terms from all processes"
    terms = set()
    for i in range(1, size):
        terms.update(comm.recv(source=i))
    terms = list(terms)
    print "\nRank", rank, "Successfully collected all terms"
    for i in range(1, size):
        print "\nRank", rank, "Trying to send terms to", i
        comm.send(terms, dest=i)

if rank != 0:
    initial_time = time.time()
    print "\nRank", rank, "Updating terms..."
    terms = comm.recv(source=0)
    document_manager.update_terms(terms)
    print "\nRank", rank, "Time taken:", time.time() - initial_time, "s"

    print "\nRank", rank, "Vectorizing documents..."
    initial_time = time.time()
    document_manager.vectorize_documents()
    print "\nRank", rank, "Time taken:", time.time() - initial_time, "s"

    documents = document_manager.get_documents()
    comm.send(documents, dest=0)

if rank == 0:
    documents = []
    print "\nRank", rank, "Recollecting documents from all processes"
    for i in range(1, size):
        documents.extend(comm.recv(source=i))
    print "\nRank", rank, "Successfully collected all documents"

initial_time = time.time()
centers = None

if rank == 0:

    print "\nRank", rank, "Starting K-means Algorithm...\n"
    centers = Cluster.pick_centers(documents, 4)

    while True:
        comm.bcast(centers, root=0)
        clusters = [[] for i in range(len(centers))]
        for i in range(1, size):
            new_clusters = comm.recv(source=i)
            for j in range(len(new_clusters)):
                clusters[j].extend(new_clusters[j])
        print clusters
        new_centers = Cluster.reevaluate_centers(clusters)
        if Cluster.has_converged(centers, new_centers):
            print "\nRank", rank, "ALL DONE!!!!\n"
            comm.bcast(-1, root=0)
            break
        centers = new_centers

if rank != 0:
    centers = comm.bcast(centers, root=0)
    print "\nRank", rank, "Receiving centers from zero\n"
    while centers != -1:
        clusters = Cluster.reevaluate_clusters(documents, centers)
        comm.send(clusters, dest=0)
        centers = comm.bcast(centers, root=0)

if rank == 0:
    print "\nRank", rank, "Time taken:", time.time() - initial_time, "s"
    cluster_names = Cluster.get_center_terms(terms, new_centers)
    i = 0
    for cluster in clusters:
        print
        print "Documents in cluster", cluster_names[i], '\n'
        for document in cluster:
            print document.get_name()
        i = i + 1
