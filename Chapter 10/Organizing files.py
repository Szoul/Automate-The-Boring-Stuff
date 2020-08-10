import shutil, os
from pathlib import Path

dir1_path = Path("C:/Users/Acer PC/Desktop/Python/Automate-The-Boring-Stuff/Chapter 10/dir1")
dir2_path = Path("C:/Users/Acer PC/Desktop/Python/Automate-The-Boring-Stuff/Chapter 10/dir2")
filename = "a_moving_file_title.txt"

# shutil.copy(source, destination) copies a file (File_path, New_Directory_path [/new_filename])
    # shutil.copytree(source, destination) will copy the whole folder, with anything it contains [or creates a new folder]
    # if the file(name) already exists at destination it will overwrite the file
shutil.copy(dir1_path/filename, dir2_path/"wello, horld.txt")

# similar: shutil.move(source, destination)
    # though be careful when moving to non-existing folders and with naming



# Deleting files with os
    # os.unlink(Path)   - delete file at path
    # os.rmdir(Path)    - delete an EMPTY folder at path
    # os.rmtree(Path)   - delete folder and its contents at path
''' ---> be careful with deleting files, better test with a simple [print(filename)] if you are targeting the right Path '''

dirname = Path("C:/Users/Acer PC/Desktop/Python/Automate-The-Boring-Stuff/Chapter 10/New_Directory/Even_Newer_Directory")
# os.makedirs(dirname)
# print (dirname)
    # os.rmdir(dirname)
# print (dirname.parent)
    # os.rmdir(dirname.parent)

''' alternative: sent2trash module (so files will get moved to trash instead of deleted permamently)'''


# using os.walk() to walk through a directory tree
# it returns the current folder name, its contents(subfolders + contents and files)    
# cwd is not changed while running this function

for folderName, subfolders, filenames in os.walk(os.getcwd()):
    print('\nThe current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)
print ("")
print (list(os.walk(os.getcwd())))
print ("\n\n")


# compressing/creating an archive file with .zip with the zipfile module
import zipfile

cwd = Path("C:/Users/Acer PC/Desktop/Python/Automate-The-Boring-Stuff/Chapter 10")
exampleZip = zipfile.ZipFile(cwd/"example.zip")
print (exampleZip.namelist())
zip_info = exampleZip.getinfo("zip_file.txt")
print (zip_info.file_size)
print (zip_info.compress_size)
exampleZip.close()

# extract files
    # exampleZip = zipfile.ZipFile(cwd/"example.zip")
    # examleZip.extractall()                            // to current cwd or .extractall([directory])
    # exampleZip.extract("[item in .namelist()], [directory/cwd])
    # exampleZip.close()

# add files (new file, named <new.zip> with the contents of <a_random_file.txt>)
    # newZip = zipfile.ZipFile("new.zip", "w")                                            --> same as writing new files, "w" will replace, "a" will append
    # newZip.write('a_random_file.txt', compress_type=zipfile.ZIP_DEFLATED)
    # newZip.close()