import os
import file_ext
from pathlib import Path

EXCL = ['__pycache__']

def main(dir_path = os.path.dirname(os.path.realpath(__file__))):
    getFileFolderList(dir_path)
    createFolders(dir_path)

def createFolders(path):
    for folder_name in file_ext.EXT:
        Path(path + "/" + folder_name).mkdir(parents=True, exist_ok=True)

def getFileFolderList(path):
    names_list = os.listdir(path)
    for folder_name in file_ext.EXT:
        if folder_name in names_list:
            names_list.remove(folder_name)
    return names_list

if __name__ == "__main__":
    # main()
    print()