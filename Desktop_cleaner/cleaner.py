import os
import file_ext
import shutil
from pathlib import Path

# PATH_CURRENT_SCRIPT = os.path.realpath(__file__)
# PATH_CURRENT_DIR = os.path.dirname(os.path.realpath(__file__)) + '/file_ext.py'
LIST_EXCLUSION = ['__pycache__', 'file_ext.py', 'cleaner.py']

def main(dir_path = os.path.dirname(os.path.realpath(__file__))):
    """Execute all the functions."""
    names_list = getFilesFoldersList(dir_path)
    createFolders(dir_path)
    moveFilesFolders(names_list)

def createFolders(path):
    """Create all the folders needed if they don't already exist."""
    for folder_name in file_ext.EXT:
        Path(path + "/" + folder_name).mkdir(parents=True, exist_ok=True)

def getFilesFoldersList(path):
    """Return a list of string with all the names of files and folders in the target directory."""
    dir_list = os.listdir(path)
    names_list = [x for x in dir_list if x not in LIST_EXCLUSION]
    for folder_name in file_ext.EXT:
        if folder_name in names_list:
            names_list.remove(folder_name)

    return names_list

def moveFilesFolders(names_list):
    """Move all the files and folders listed in the target directory to their new folder according to their type/extension."""
    moved_list = []
    moved = False # Bool used to stop loop if the file was moved (in order to avoid useless loops)
    for name in names_list:
        for folder, ext_list in file_ext.EXT.items():
            if ext_list != []:
                for ext in ext_list:
                    if name.endswith(ext):
                        print("name =", name)
                        shutil.move(name, './' + folder + '/' + name)
                        moved_list.append(name)
                        moved = True
                        break # stop the "for ext in ext_list" loop
            if moved:
                moved = False
                break # stop the "for folder, ext_list in file_ext.EXT" loop

    unmoved_list= [x for x in names_list if x not in moved_list] #list of unmoved files/folders

    for name in unmoved_list: # move all files without extension or folder to the OTHERS folder
        shutil.move(name, './OTHERS/' + name)

if __name__ == "__main__":
    loop = True
    while loop:
        dir_path = input("Enter the path of the folder to clean (enter . for current folder): ")
        if(dir_path == ""):
            main()
            loop = False
        else:
            if(os.path.exists(dir_path)):
                main(dir_path)
                loop = False
            else:
                print("\nThis folder doesn't exist. Try Again !\n")
    print("Directory cleaned !")