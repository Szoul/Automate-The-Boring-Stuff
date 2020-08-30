#! python 3.8.3
# goal: what is %s%% string replacement, what can it be used for, is it the same/similar to f-strings

"""
== formatting values into strings

The %s token allows me to insert (and potentially format) a string.
Notice that the %s token is replaced by whatever I pass to the string after the % symbol. 
Notice also that I am using a tuple here as well (when you only have one string using 
a tuple is optional) to illustrate that multiple strings can be inserted and formatted in one statement.
"""

name = "Simon"
age = 22
example = "Hello, my name is %s, I am %d years old" % (name, age)                       # %s - string | %d - digit | %f - float
print (example)
example2 = f"Hello, my name is {name}, I am {age} years old"
example3 = "Hello, my name is {name}, I am {age} years old".format(name = name, age = age)
print (example2)
print (example3)

# different ways of string interpolation, though i do not know (yet) what the exact difference is/ or what is smarter to use in which case


print ("____________________________________________________________________")

# from Automate-the-boring-stuff - Chapter 11 (debuging)
# factorialLog.py (already corrected to work as intended)
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname) s -  %(message)s')    # prints out a timestamp - "DEBUG" - whatever message it is given
logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s%%)'  % (n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s%%)'  % (n))
    return total

print(factorial(5))
logging.debug('End of program')
print ("___________________________________\n")

# change to f-strings:
"""
from logging module - how to:

    The following message format string will log the time in a human-readable format, 
    the severity of the message, and the contents of the message, in that order:

    '%(asctime)s - %(levelname)s - %(message)s'

--> probably cannot chane to f-string
"""
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname) s -  %(message)s')    # cant change that because of above
logging.debug("Start of program")

def factorial2(n):
    logging.debug(f"Start of factorial {n}")
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug(f"i is {i}, total is {total}")
    logging.debug(f"End of factorial {n}")
    return total

print(factorial2(5))
logging.debug('End of program')