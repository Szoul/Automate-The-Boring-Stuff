# Any test/file named here will be in following folder (except for this one)
# C:\Users\Acer PC\Desktop\Python\Automate-The-Boring-Stuff\Chapter 9

# "C:\"  == root - folder
#  --> Windows Path-system uses "\", Linux-based uses "/" to seperate directories
#          --> which is why filenames on windows cannot contain a "\"
#  --> the <pathlib> module will work on any of these operating systems

from pathlib import Path                                    #or use pathlib.Path if you only import pathlib

example_path = Path("This", "is", "a", "Path")              #run this on windows shell to return a WindowsPath object || on Linux a PosixPath object (Unix-based)
print (example_path)

# the "/" operator can join two Path-objects or a Path-Object with a non-path object:
example_path = Path("This")/"is"/"a"/"Path"                                 #to be precise: the function first connects "this" and "is" - then adds the next word to the existing Path-Object (which is why "a"/"Path" will not initially join since none are a Path-object)
print (example_path)                                                        #theoretically using the "join" method or just concetating the strings with a "\" would work - but only on windows (Therefore: Path-method)


#cwd - current working directory:
cwd = Path.cwd()
print (cwd)

import os
# os.chdir([new Path]) - changes current working directory to the new path  
        # changing the cwd while running a programm might lead to bugs --> therefore Path-function does not have this function

home_directory = Path.home()                            # scripts&files need permission to read/write files, which they usually do if within the home directory
print (home_directory, "\n")



# absolut paths:  full path, beginning from root folder ("C"); 
# relative paths: relative from current cwd

# .[file] <-- the "." refers to this directory (replaces Path to this directory)
# ..[file] <-- ".." refers to parent folder

# Example:    .\Python\Automate-The-Boring-Stuff\Chapter 9 == C:\Users\Acer PC\Desktop\Python\Automate-The-Boring-Stuff\Chapter 9
#             ..\Python == C:\Users\Acer PC\Desktop
#             [relative Path] == [absolut Path]
if Path.cwd().is_absolute():
    print ("the cwd-function returns an absolute path")
if example_path.is_absolute():
    print ("This path does not start/is not in the root")   #will not be printed
if (Path.cwd()/example_path).is_absolute():
    print ("relative path usually refers to 'relative to cwd'")
# os.path.abspath([Path]) returns the absolute path, even if input is a relative path
print (os.path.abspath("."))            # == cwd
# os.path.relpath([Path],[Start]) returns a relative path from Start - Path
print (os.path.relpath(Path.home(), Path.cwd()) + "\n") #from cwd to "C:\Users\Acer Pc"



r'''
naming:
    C:/Users/Acer PC/Desktop/Python/Automate-The-Boring-Stuff/Chapter 9/random_file.txt

    Drive (only Windows) =     C:       
    Anchor (root folder) =    C:\
    Parent = Users/Acer PC/Desktop/Python/Automate-The-Boring-Stuff/Chapter 9
    Name = random_file.txt
        Stem = random_file
        Suffix = .txt
'''
random_file = Path("C:/Users/Acer PC/Desktop/Python/Automate-The-Boring-Stuff/Chapter 9/random_file.txt")
print (random_file.drive)
print (random_file.anchor)
print (random_file.parent)
print (random_file.parents[1])          # path.parents[0] == path.parent
print (random_file.name)
print (random_file.stem)
print (random_file.suffix)
print ("")                              #os.path.[basename/dirname] and Path.split(os.sep) also are good for that



#creating new folders:
new_test_folder = Path("C:/Users/Acer PC/Desktop/Python/Automate-The-Boring-Stuff/Chapter 9/New_Test_Folder")
if not new_test_folder.exists():
    os.makedirs(new_test_folder)                     #would give an error [FileExistsError] if folder already exists
else:
    print ("New_Test_Folder already exists")



#file-Sizes and folder Contents:s
# os.path.getsize([path])   returns filesize in bytes
# os.listdir([path])        returns a list of filenames for each file in path
total_Size = 0
for filename in os.listdir("C:\\Users\\Acer Pc\\Desktop\\Python\\Automate-The-Boring-Stuff"):
    total_Size += os.path.getsize(os.path.join("C:\\Users\\Acer Pc\\Desktop\\Python\\Automate-The-Boring-Stuff", filename))             #join a different file each iteration until all file in directory are counted
print ("Size of Automate_the_boring_stuff folder in bytes: " + str(total_Size))



# the <<glob>> methods
# for: Path objects; usefull if working with specific files
# like a simplefied form of regular expressions 
# returns: a generator object, easily viewed with list()
test_path = Path("C:/Users/Acer PC/Desktop/Python/Automate-The-Boring-Stuff")
print ("")
print(list(test_path.glob("*")))                                                                # * == multiple of any characters == all files 
                                                                                                # works similar to regexes
                                                                                                # *.py == all python files
                                                                                                # ? can replace any single character; * and ? are combineable
                                                                                                # Chapter ?  == any file/directory with the name "Chapter " and a single character at the end
print ("")

for path_object in test_path.glob("Chapter ?"):                                                 #os.listdir(test_path) == test_path.glob("*"), though it returns different type objects
    print (path_object)
print ("")


# checking for validity
# [path].exists()
    # [Drive].exists() to check for USB-Stick for example
# [path].is_file()
# [path].is_dir()
# returns boolean

