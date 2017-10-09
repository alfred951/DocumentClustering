from os import listdir
from os.path import join, isfile


class DocumentManager:

    def __init__(self, path):
        self.path = path
        self.files = []

    def get_path(self):
        return self.path

    def get_filenames(self):
        self.files = [f for f in listdir(self.path) if isfile(join(self.path, f))]
        return self.files

    def generate_dictionary(self):
        # for f in self.files:
            wordcount = []
            # file = open(self.path + f, "r+")
            file = open(self.path + self.files[0], "r+")
            word = file.read().split()
            print len(word)
            print word
            for i in range(len(word)):
                if wordcount.index():
                    wordcount.append(word)
            print len(wordcount)

