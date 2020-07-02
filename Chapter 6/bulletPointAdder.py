#! python 3.8.3
#bulletPointAdder.py - adds a '* ' to the start of each line of input

import pyperclip

text = str(pyperclip.paste())
text_list = text.split("\n")
for x in range(len(text_list)):
    text_list[x] = "* " + text_list[x]
text = "\n".join(text_list)

pyperclip.copy(text)