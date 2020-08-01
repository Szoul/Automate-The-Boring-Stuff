# How to save Variables with the shelve(binary) and pprint module(create new python file)

import shelve

shelve_file = shelve.open("mydata")                 # cannot pass Path object to this function, has to call filename as a string
colours = ["red","green","blue"]
shelve_file["colours"] = colours                    # like a dictionary "colours":colours
shelve_file.close()

# mydata.bak, mydata.dat, and mydata.dir are created in cwd to store information
# once opened reading and writing can be done both

shelve_file = shelve.open("mydata")
print (type(shelve_file))
print (shelve_file["colours"])
shelve_file.close()

# just like dictionaries, .keys() and .values() work on these objects
# it does NOT return a list value (even if it looks like one if printed), but it can be converted to one

shelve_file = shelve.open("mydata")
print (shelve_file.keys())
print (list(shelve_file.keys()))
print (shelve_file.values())
print (list(shelve_file.values()))

# Plaintext is useful to create files that are read in a text-editor
# Python data for example is better stored with the shelve module

print ("_______________________________________________________________________________")

import pprint

colours2 = [{"bright":"white","dark":"black"},{"basic":"blue, red, yellow"}]            # data which is to be safed in a new file
print (pprint.pformat(colours2))                                                        # returns a string that can be written into a .py file
file_obj = open("colours.py", "w")                                                      # open new .py file in cwd named colours
file_obj.write("colours = " + pprint.pformat(colours2) + "\n")                          # write into that pythin file: "colours = [content of colours2] [newline in the python script]"
file_obj.close()

# since it is in write mode, it will overwrite the file each time this is executed 
# --> append new content

file_obj = open("colours.py", "a")
for i in range (2,10):
    file_obj.write(f"colours{i} = " + pprint.pformat(colours2) + "\n")

# since this script will "overwrite" its content  and then append, it will have the same contents each time this script is run [be careful with endless loops!]


''' open questions:

        How to create and work on a new file (text/python  file) which is not in current cwd:
            obviously use the [path].filename.suffix or [relativepath to cwd].filename.suffix when opening a file
            since shelve doesnt accept PATH objects, i probably have to use os / write it out manually
'''
print ("________________________________________________________________")

import os

# test: creating and writing a new file in New_Test_Folder, then save its content with shelve in that folder

current_path = os.path.dirname(__file__)
print (current_path)
rel_path = os.path.relpath(".\\New_Test_Folder", current_path)
abs_path = os.path.abspath(rel_path)
print (rel_path)
print (abs_path)

test_list = [1,2,3,4]
test_file = open((abs_path + "\\testfile_from_intro_3.py"), "w")                    # works!!! (don't forget to escape a backslash when not using PATH objects)
test_file.write("test_list2 = " + pprint.pformat(test_list)+ "\n")
test_file.close()

# access the testfiles contents and store them in the same directory as it with the shelve module
'''
problem: when importing modules/files it will only access "current directory, the directory that the entry-point script is running from, and sys.path"
Stackoverflow (4383571)
However, you can add to the Python path at runtime:

# some_file.py
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '/path/to/application/app/folder')

import file
'''
print ("__________________________________________________________________________")
import sys

sys.path.insert(1, abs_path)
from testfile_from_intro_3 import test_list2

# from google: what is a __pycache__ ; since it was create in the new_test_folder 
# A __pycache__ folder is created when you use the line: import file_name. or try to get information from another 
# file you have created. This makes it a little faster when running your program the second time to open the other file.

test_shelve = shelve.open((abs_path + "\\testfile_from_intro_3"))
test_shelve["numbers"] = test_list2
test_shelve.close()

test_shelve = shelve.open((abs_path + "\\testfile_from_intro_3"))
print (list(test_shelve["numbers"]))
test_shelve.close()

