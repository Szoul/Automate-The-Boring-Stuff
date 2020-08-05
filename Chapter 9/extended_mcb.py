'''
Extend the multi-clipboard program in this chapter so that it has a delete 
<keyword> command line argument that will delete a keyword from the shelf. 
Then add a delete command line argument that will delete all keywords.

Therefore: Code below is mainly copied from Chapter 9 - Automate the boring stuff
    #On Windows running this as a batch script with commands as Input should work
'''

#! python 3.8.3
# (mcb.pyw - Saves and loads pieces of text to the clipboard.- copied from chapter 9)   TODO  --> project- extended_mcb.py - description above
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.

import shelve, pyperclip, sys
mcbShelf = shelve.open('mcb')

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':                        # sys.argv[1] == first commandline argument (save, list or a keyword) | [2] is used to save the argument as a new keyword (and clipboard as value)
    mcbShelf[sys.argv[2]] = pyperclip.paste()

# delete [keyword] - [1] = delete [2] = <keyword>
# if with one keyword: regex(r"^[(delete )](.*)") - second group = new keyword
elif len(sys.argv) == 3 and sys.argv[1].lower() == "delete":
    del mcbShelf[sys.argv[2]]

elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))

# delete all
    elif sys.argv[1] == "delete all":
        mcbShelf.clear()

    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()