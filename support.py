from os import walk

def import_folder(path):

    for information in walk(path):
        print(information)

import_folder('./graphics/character/run')