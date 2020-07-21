#"how to keep an idiot busy for hours with pyip"
'''
    Ask the user if they’d like to know how to keep an idiot busy for hours.
    If the user answers no, quit.
    If the user answers yes, go to Step 1.
'''

import pyinputplus as pyip
#help(pyip)
#help(pyip.inputYesNo)
#help(pyip.parameters)

while True:
    response = pyip.inputYesNo(prompt = "Want to know how to keep an idiot busy for hours?\n", )
    if response == "no":
        print ("Ok, have a nice day!")
        break


            #https://pyinputplus.readthedocs.io/en/latest/ fo all pyip functionalities