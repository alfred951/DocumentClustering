from os import listdir
from os.path import join, isfile


class DocumentManager:

    def __init__(self):
        self.path = ""

    def getPath(self):
        return self.path

    def get_filenames(self):
        files = [f for f in listdir(self.path) if isfile(join(self.path, f))]
        return files
