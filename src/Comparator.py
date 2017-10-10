import math
import numpy as np


def calculate_jaccard_distance(document_a, document_b):
    document_a = np.asarray(document_a)
    document_b = np.asarray(document_b)
    print document_a.shape
    print document_b.shape
    result = np.dot(document_a, document_b)
    result = result / np.cross(document_a, document_b, axis=0)
    return result


def calculate_euclidean_distance(document_a, document_b):
    result = 0;
    for x, y in zip(document_a, document_b):
        result += math.pow(x - y, 2)
    result = math.sqrt(result)
    return result
