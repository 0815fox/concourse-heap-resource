import os

def get_newest(path):
    version = 0
    if not os.path.exists(path + str(version)):
        os.makedirs(path + str(version))
    while os.path.exists(path + str(version)):
        version = version + 1
    print("newest version " + str(version))
    return version - 1
