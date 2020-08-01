from pathlib import Path
import os

# this will cover plaintext files such as [.txt] and [.py] files
# binary files like [.pdf] will look like scrambled rubbish, if watched throuh the normal text_editor since they need further intepretation/processing
# example for binary files is covered in Into(3)



p = Path("spam.txt")
number_of_words = p.write_text("Hello, world!")                              # .write_text() creates new .txt file (in cwd) with the content "Hello, world!"/ or overwrites an existing one
print (number_of_words)                                                      # returns number of strings (as a string)
text = p.read_text()                                                         # .read_text() calls and returns text within that file
print (text)
print ("\n\n")

# more commonly one uses open() read() write() and close() functions to interact with a File object
cwd_path = Path(r"C:/Users/Acer PC/Desktop/Python/Automate-The-Boring-Stuff/Chapter 9")


helloFile = open(cwd_path/"spam.txt", "r")              # == helloFile = open('C:\\Users\\Acer PC\\Desktop\\Python\\Automate-The-Boring-Stuff\\Chapter 9\\'spam.txt')
                                                        # the [, "r"] is the default option, "reading plaintext mode"
                                                        # open() returns a File - type object - which you can use to read/interact with

helloContent = helloFile.read()                         # returns the content of a file as a single sting value
helloContent_List = helloFile.readlines()               # returns a list with a string for each line of text
print (helloContent)
print (helloContent_List)                               # This will be empty though if the file has already been read with .read() for example

# stackoverflow(28873349)
'''
When you do current.read(), you consume the contents of the file, so a subsequent current.readlines() returns an empty list.
'''

helloFile.close()                                       # close first before changing working mode 
helloFile = open(cwd_path/"spam.txt", "w")              # open in write mode; [a] instead of [w] opens append mode (over-writing or appending)
helloFile.write("Hello, World!\nHow are you?")
helloFile.close()

helloFile = open(cwd_path/"spam.txt", "r")
print ("\n" + helloFile.read())
