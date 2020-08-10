#! python 3.8.3
# deleting_unneeded_files.py - search and print any file with size > x, within a certain directory

# TODO
    # walk through folder tree with os.walk()
    # get filesize of any file with os.path.getsize()
    # compare with a set size_threshhold
    # print (or delete) if it exceeds threshhold

import os

directory_to_search = "C:\\Users\\Acer PC\\Desktop\\Python\\Automate-The-Boring-Stuff\\Chapter 10"
threshhold = 1000

for folders, subfolders, files in os.walk(directory_to_search):
    for filename in files:
        filesize = os.path.getsize(folders)
        if filesize > threshhold:
            print ("file to delete:")                                               # replace with actual path and delete with os.unlink()
            print (folders + "\\" + filename)
            print ("Size of the file = " + str(filesize))
            print ("\n")