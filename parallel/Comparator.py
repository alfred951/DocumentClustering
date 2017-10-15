import math
import numpy as np


def calculate_cosine_distance(document_a, document_b):
    document_a = np.asarray(document_a)
    document_b = np.asarray(document_b)
    numerator = np.dot(document_a, document_b)
    denominator = np.linalg.norm(document_a) * np.linalg.norm(document_b)
    result = 1 - (numerator / denominator if denominator else 0)
    return result


def calculate_euclidean_distance(document_a, document_b):
    result = 0
    for x, y in zip(document_a, document_b):
        result += math.pow(x - y, 2)
    result = math.sqrt(result)
    return result


def calculate_jaccard_distance(document_a, document_b):
    document_a = np.asarray(document_a)
    document_b = np.asarray(document_b)
    numerator = np.dot(document_a, document_b)
    denominator = np.power(np.linalg.norm(document_a), 2) + np.power(np.linalg.norm(document_b), 2) - numerator
    result = 1 - (numerator / denominator if denominator else 0)
    return result

