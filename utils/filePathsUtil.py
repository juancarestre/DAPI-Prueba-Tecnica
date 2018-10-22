from os import listdir
from os.path import isfile, join

class filesInFolder(object):
    def __init__(self,folderPath, *args, **kwargs):
        self.folderPath=folderPath
    def getPaths(self):
        onlyfiles = ['{}{}'.format(self.folderPath,f) for f in listdir(self.folderPath) if isfile(join(self.folderPath, f))]
        return onlyfiles

if __name__=="__main__":
    paths=filesInFolder('../resources/images/').getPaths()
    print(paths)