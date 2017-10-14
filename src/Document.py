import numpy as np


class Document:
    def __init__(self, name, terms):
        self.name = name
        self.terms = terms

    def get_name(self):
        return self.name

    def get_terms_as_array(self):
        return np.asArray(self.terms)

    def get_terms(self):
        return self.terms

    def vectorize(self, all_terms):
        document_vector = [0] * len(all_terms)
        for key, value in self.terms.items():
            document_vector[all_terms.index(key)] = value
        self.terms = document_vector
