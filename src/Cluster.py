import random
import numpy as np
import Comparator


def reevaluate_clusters(documents, centers):
    print type(centers)
    print "Reevaluating clusters..."
    cluster = []
    for center in range(len(centers)):
        cluster.append([[0]])
    for document in documents:
        group = []
        print "-------------------------------"
        best_center_distance = 999999
        best_center = -1
        center_index = 0
        for center in centers:
            center_distance = Comparator.calculate_cosine_distance(document, center)
            print "Center distance:", center_distance
            if best_center_distance > center_distance:
                best_center_distance = center_distance
                best_center = center_index
            center_index = center_index + 1
        print "Best center key:", best_center
        group[best_center].append(document)
    cluster.append(group)
    return cluster


def reevaluate_centers(clusters):
    print '\n'
    print "Reevaluating centers..."
    new_centers = []
    for cluster in clusters:
        cluster = np.asarray(cluster)
        var = list((np.mean(cluster, axis=0)))
        new_centers.append(var)
        new_centers = list(new_centers)
    print "New centers:", new_centers
    return new_centers


def has_converged(centers, old_centers):
    return set([tuple(a) for a in centers]) == set([tuple(a) for a in old_centers])


def find_centers(documents, k):
    old_centers = random.sample(documents, k)
    centers = random.sample(documents, k)
    print "Choosing random centroids:"
    print centers
    while not has_converged(centers, old_centers):
        old_centers = centers
        clusters = reevaluate_clusters(documents, centers)
        centers = reevaluate_centers(clusters)
    return centers, clusters


