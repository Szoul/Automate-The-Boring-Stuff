#! python 3.8.3
# selective_copy.py - copys files of a certain suffix from the original folder(and its subfolders) to another directory

# TODO
    # Loop
        # walk through a directory-tree with os.walk
        # regex to select files with the named suffix
        # shutil.copy() files to new directory

    # optional: make it a function that recieves the original and the new directiory, as well as the suffix as an argument


def copy_suffixfiles_to_folder (original_directory, goal_directory, suffix):
    import os, shutil, re
    from pathlib import Path

    regex = re.compile(rf"(.*?)\.{suffix}$")

    for foldername, subfoldername, filename in os.walk(original_directory):                     # filename is a list of filenames in current folder, if current folder is empty it will return an empty list
        for files in filename:
            match = regex.search(files)
            if match != None:
                filename_to_move = match.group()
                foldername = foldername.replace("\\","/")                                       #convert forward slashes to backwards slashes in order to use with the Path module, because Windows path system is just perfect 
                file_to_move_path = Path(f"{foldername}/{files}")
                # print (file_to_move_path)
                # print (goal_directory)
                shutil.copy(file_to_move_path, goal_directory)
                print (f"copying <{files}> to goal directory")

from pathlib import Path
suffix = "txt"
original_directory = Path("C:/Users/Acer PC/Desktop/Python/Automate-The-Boring-Stuff/Chapter 10/dir1")
goal_directory = Path ("C:/Users/Acer PC/Desktop/Python/Automate-The-Boring-Stuff/Chapter 10/dir2/selective_copy_goal_dir")

copy_suffixfiles_to_folder(original_directory, goal_directory, suffix)