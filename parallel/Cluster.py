import random
import numpy as np
import Comparator
import operator


def reevaluate_clusters(documents, centers):
    clusters = [[] for i in range(len(centers))]
    for document in documents:
        best_center_distance = 99999
        best_center_index = -1
        i = 0
        for center in centers:
            center_distance = Comparator.calculate_cosine_distance(document.get_terms(), center)
            if center_distance < best_center_distance:
                best_center_distance = center_distance
                best_center_index = i
            i = i+1
        clusters[best_center_index].append(document)
    return clusters


def reevaluate_centers(clusters):
    new_centers = []
    for cluster in clusters:
        document_terms = list(map(lambda x: x.get_terms(), cluster))
        document_terms = np.asarray(document_terms)
        var = list((np.mean(document_terms, axis=0)))
        new_centers.append(var)
        new_centers = list(new_centers)
    return new_centers


def has_converged(centers, old_centers):
    return set([tuple(a) for a in centers]) == set([tuple(a) for a in old_centers])


def get_center_terms(terms, centers):
    center_terms = []
    for center in centers:
        index, value = max(enumerate(center), key=operator.itemgetter(1))
        center_terms.append(terms[index])
    return center_terms


def find_centers(terms, documents, k):
    old_centers = random.sample(documents, k)
    centers = random.sample(documents, k)

    new_centers = []
    for center in old_centers:
        center = center.get_terms()
        new_centers.append(center)
    old_centers = new_centers

    new_centers = []
    for center in centers:
        center = center.get_terms()
        new_centers.append(center)
    centers = new_centers

    while not has_converged(centers, old_centers):
        old_centers = centers
        print "Doing a k-mean iteration..."
        clusters = reevaluate_clusters(documents, centers)
        centers = reevaluate_centers(clusters)
    center_names = get_center_terms(terms, centers)
    return centers, clusters, center_names


def pick_centers(documents, k):
    centers = random.sample(documents, k)
    new_centers = []
    for center in centers:
        center = center.get_terms()
        new_centers.append(center)
    centers = new_centers
    return centers;

