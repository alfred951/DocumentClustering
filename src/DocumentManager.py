from os import listdir
from os.path import join, isfile


class DocumentManager:
    def __init__(self, path):
        self.path = path
        self.files = []
        self.terms = set()
        self.wordcount = []
        self.stopwords = ['a', 'able', 'about', 'across', 'after', 'all', 'almost', 'also', 'am', 'among',
                          'an', 'and', 'any', 'are', 'as', 'at', 'be', 'because', 'been', 'but', 'by', 'can',
                          'cannot', 'could', 'dear', 'did', 'do', 'does', 'either', 'else', 'ever', 'every',
                          'for', 'from', 'get', 'got', 'had', 'has', 'have', 'he', 'her', 'hers', 'him', 'his',
                          'how', 'however', 'i', 'if', 'in', 'into', 'is', 'it', 'its', 'just', 'least', 'let',
                          'like', 'likely', 'may', 'me', 'might', 'most', 'more', 'must', 'my', 'neither', 'no', 'nor',
                          'not', 'of', 'off', 'often', 'on', 'only', 'or', 'other', 'our', 'own', 'rather', 'said',
                          'say', 'says', 'she', 'should', 'since', 'so', 'some', 'than', 'that', 'the', 'their',
                          'them', 'then', 'there', 'these', 'they', 'this', 'tis', 'to', 'too', 'twas', 'us', 'up',
                          'very', 'wants', 'was', 'we', 'were', 'what', 'when', 'where', 'which', 'while', 'who',
                          'whom', 'why', 'will', 'with', 'would', 'yet', 'you', 'your']

    def get_path(self):
        return self.path

    def get_filenames(self):
        self.files = [f for f in listdir(self.path) if isfile(join(self.path, f))]
        self.files.sort()
        return self.files

    def count_words(self):
        for f in self.files:
            file = open(self.path + f, "r+")
            document_wordcount = {}
            words = file.read().lower().split()
            self.terms.update(words)
            for word in words:
                if word not in self.wordcount:
                    document_wordcount[word] = 1
                else:
                    document_wordcount[word] += 1
            self.wordcount.append(document_wordcount)
        print(self.wordcount)


    def generate_dictionary(self):
        for f in self.files:
            file = open(self.path + f, "r+")
            # file = open(self.path + self.files[0], "r+")
            words = file.read().lower().split()

    def remove_stopwords(self):
        self.terms = self.terms.difference(self.stopwords)
        for key in self.stopwords:
            self.wordcount.pop(key, None)

    def get_terms(self):
        print "Terms: ", len(self.wordcount.keys())
        print "Terms + Count: ", len(self.terms)
        return self.terms

