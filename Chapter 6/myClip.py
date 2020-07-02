#! python 3.8.3 32-bit
# myClip.py - A multi-clipboard program

TEXT = {"agree":""" Fine for me""",
        "disagree":"""I'm sorry, that is not possible for me right now""",
        "busytill":"""I won't have time until"""}

import sys, pyperclip

if len(sys.argv) < 2:
    print ("Usage: python mclip.py [keyphrase] - this will copy the corresponding phrase text")
    sys.exit()
keyphrase = sys.argv[1]

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for ' + keyphrase + ' copied to clipboard.')
else:
    print('There is no text for ' + keyphrase)


#what is and how to create: bash script; use this script effectivly, 
#how to use sys.argv effectively