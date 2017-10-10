import re
from os import listdir
from os.path import join, isfile
from stemming.porter2 import stem


class DocumentManager:
    def __init__(self, path):
        self.path = path
        self.files = [f for f in listdir(self.path) if isfile(join(self.path, f))]
        self.files.sort()
        self.terms = set()
        self.documents = []
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
        return self.files

    def count_words(self):
        for f in self.files:
            document = open(self.path + f, "r+")
            wordcount = {}
            words = document.read().lower().split()
            for i in range(len(words)):
                regex = re.compile('[^a-z]')
                words[i] = regex.sub('', words[i])
                words[i] = stem(words[i])
            for word in words:
                if word != '':
                    if word not in wordcount:
                        wordcount[word] = 1
                    else:
                        wordcount[word] += 1
            self.terms.update(words)
            wordcount = self.remove_stopwords(wordcount)
            self.documents.append(wordcount)
        self.terms = self.terms.difference(self.stopwords)
        self.terms.remove('')

    def remove_stopwords(self, wordcount):
        for key in self.stopwords:
            wordcount.pop(key, None)
        return wordcount

    def get_terms(self):
        print "Documents:", len(self.documents)
        print "Terms:", len(self.terms)
        print self.terms
