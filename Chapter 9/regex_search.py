'''
Write a program that opens all .txt files in a folder and searches for any 
line that matches a user-supplied regular expression. The results should be 
printed to the screen.
'''

#! python 3.8.3
# regex_search.py

from pathlib import Path
import glob, re

# user regex input
print ("Enter your matching pattern:")
user_input = input()
regex = re.compile (rf"{user_input}")

# search all .txt files in cwd
    # match content with user input regex
cwd_path = Path("C:/Users/Acer PC/Desktop/Python/Automate-The-Boring-Stuff/Chapter 9")  # or os.getcwd()
txt_files_list = list(cwd_path.glob("*.txt"))
dict_of_matches = {}

for file_nmb in range (len(txt_files_list)):
    current_file = open(txt_files_list[file_nmb])
    content_list = current_file.readlines()
    dict_of_matches.update({txt_files_list[file_nmb]:None})

    for line in range (len(content_list)):
        match = regex.search(content_list[line])
        if match != None:
            if dict_of_matches[txt_files_list[file_nmb]] == None:
                dict_of_matches[txt_files_list[file_nmb]] = str(line+1)
            else:
                dict_of_matches[txt_files_list[file_nmb]] += (" | " + str(line+1))
    
    current_file.close()


# return results ("name file and line-number") print to screen
print ("Your pattern matches with following lines in each file:")
for key in dict_of_matches.keys():
    filename = key.name
    print (filename + " line(s): " + str(dict_of_matches[key]))


