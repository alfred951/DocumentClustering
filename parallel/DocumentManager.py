import re
from stemming.porter2 import stem
from Document import Document


class DocumentManager:
    def __init__(self, path, files):
        self.path = path
        self.files = files
        self.terms = []
        self.documents = []
        self.stopwords = ['a', 'able', 'about', 'across', 'after', 'all', 'almost', 'also', 'am', 'among',
                          'an', 'and', 'any', 'are', 'as', 'at', 'be', 'because', 'been', 'but', 'by', 'can',
                          'cannot', 'could', 'dear', 'did', 'do', 'does', 'either', 'else', 'ever', 'every',
                          'for', 'from', 'get', 'got', 'had', 'has', 'have', 'he', 'her', 'hers', 'him', 'his',
                          'how', 'however', 'i', 'if', 'in', 'into', 'is', 'it', 'its', 'just', 'least', 'let',
                          'like', 'likely', 'may', 'me', 'might', 'most', 'more', 'much', 'must', 'my', 'neither',
                          'no', 'nor', 'not', 'of', 'off', 'often', 'on', 'only', 'or', 'other', 'our', 'own', 'rather',
                          'said', 'shall', 'never', 'such', 'one', 'upon', 'those', 'now',
                          'say', 'says', 'she', 'should', 'since', 'so', 'some', 'than', 'that', 'the', 'their',
                          'them', 'then', 'there', 'these', 'they', 'this', 'tis', 'to', 'too', 'twas', 'us', 'up',
                          'very', 'wants', 'was', 'we', 'were', 'what', 'when', 'where', 'which', 'while', 'who',
                          'whom', 'whose', 'why', 'will', 'with', 'would', 'yet', 'you', 'your']

    def get_path(self):
        return self.path

    def get_filenames(self):
        return self.files

    def get_documents(self):
        return self.documents

    def count_words(self):
        self.terms = set(self.terms)
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
            doc = Document(f, wordcount)
            self.documents.append(doc)
        self.terms = self.terms.difference(self.stopwords)
        self.terms.remove('')
        self.terms = list(self.terms)

    def remove_stopwords(self, wordcount):
        for key in self.stopwords:
            wordcount.pop(key, None)
        return wordcount

    def get_terms(self):
        return self.terms

    def update_terms(self, new_terms):
        self.terms = new_terms

    def vectorize_documents(self):
        for document in self.documents:
            document.vectorize(self.terms)
