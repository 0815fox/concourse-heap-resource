import os

def get_newest(path):
    version = 0
    while os.path.exists(path + str(version)):
        version = version + 1
    return version - 1
