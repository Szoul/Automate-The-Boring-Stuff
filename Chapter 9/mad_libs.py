'''
Create a Mad Libs program that reads in text files and lets the user add 
their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the 
text file. For example, a text file may look like this:

The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was
unaffected by these events.

The program would find these occurrences and prompt the user to replace them.

Enter an adjective:
silly
Enter a noun:
chandelier
Enter a verb:
screamed
Enter a noun:
pickup truck

The following text file would then be created:

The silly panda walked to the chandelier and then screamed. A nearby pickup
truck was unaffected by these events.

The results should be printed to the screen and saved to a new text file.
'''
#! python 3.8.3
# mad_libs.py - replace Keywords of a Text with input, saveed to a new textfile
# Takes a Textfile - reads contents - detects keywords - prompts user to replace keywords with input - saves changed text n new textfile

import re, copy, os
from pathlib import Path

# Textfile Input
cwd_path = Path(r"C:/Users/Acer PC/Desktop/Python/Automate-The-Boring-Stuff/Chapter 9")
text_file = Path(cwd_path/"mad_libs_example_text.txt")
opened_content = open (text_file, "r")

# Reading content
original_content = opened_content.read()
opened_content.close()
print (original_content)

# detect keywords [VERB] [NOUN] [ADJECTIVE] [ADVERB]
keyword_regex = re.compile(r"VERB|NOUN|ADVERB|ADJECTIVE", re.DOTALL)

# user input for first word - replace word - repeat loop until no more keywords
    # save new content in a different variable
content = copy.deepcopy(original_content)
match = keyword_regex.search(content)

while not (match == None):
    print ("Enter a " + match.group().lower())
    user_input = input()
    content = keyword_regex.sub(user_input, content, 1)
    print ("\n" + content)
    match = keyword_regex.search(content)

# create a new Plaintext file, save content in there
new_file = open (Path(cwd_path/"mad_libs_new_file.txt"), "w")
new_file.write(content)
new_file.close()