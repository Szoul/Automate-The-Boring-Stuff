"""
This Intro will cover: Raising Exceptions, Assertions and Logging. Aditionally Mu's debugger (and how to use it) is mentioned.
"""


# raise Exception("Message") will crash the script with the Message
# try - except error handeling to circumvent crash:

def find_an_e(string):
    if "e" in string:
        raise Exception("There is an <e>!")
    else:
        raise Exception("There is no <e>!")

hello = "Hello, World!"
try:
    find_an_e(hello)
except Exception as err:
    print (err)
    print ("the script must go on~")

# in a traceback you can see where/sometimes why the error has occured
def hi():
    bye()
def bye():
    raise Exception ("Byebye")
# hi()   uncomment to test

import traceback
try:
    hi()
except:
    error = traceback.format_exc()
    print (error)
    print ("Above this is the error traceback, without the error stopping the script")

print ("________________________________________________________-")





# Assertions to test ("sanity check") if a code is running as intended
# assert [boolean], "Message"
# if False --> AssertionError (+Message if one was written)
# like any error, it will stop the code (if not handled with a try-except statement)

def assert_number_row(number_list):
    assert number_list[0] <= number_list[-1], "the first number is not lower than the last in the list"
    print ("this will not print if an assertion error was triggered")

numbers = [1,2,3,4,5]
assert_number_row(numbers)
numbers.reverse()
try:                                                            # usually try-except statement defeats the purpose of a sanity check since the code should work as intended
    assert_number_row(numbers)                                  # it should also ONLY be used in developement, a user should not see an AssertionError
except AssertionError:                                          # it does not neccesarily replace comprehensive testing
    print (traceback.format_exc())

print ("__________________________________________________")






# Logging - log messages describe when the script has reached the message and may enlist variables/a status during that point in the sript
# for example: simple print statements to check a variable value in a loop
# the logging module can display log messages while the programm is running
    # ADVANTAGE: you can simply disable it after Debugging, and not accidently remove essential code (i.e. remove a print function that is actually needed)

#copied from Automate-the-boing-stuff chapter 11 - factorialLog.py
# find out why the factorial function does not work as intended
import logging
# logging.disable(logging.CRITICAL)                         # <-- remove to disable all logging-functions
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname) s -  %(message)s')    # prints out a timestamp - "DEBUG" - whatever message it is given
logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s%%)'  % (n))
    total = 1
    for i in range(n + 1):                                                  # --> for i in range(1, n+1) <-- it was multplying by 0
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s%%)'  % (n))
    return total

print(factorial(5))
logging.debug('End of program')

# more to the logging- module: use logging. debug|info|warning|error|critical () 
# logging info can be written into a new file with login.basicConfig(filename = "[NAME].txt", level = ...)
    # more info on chapter 11 or on module description






# Mu Debugger (IDLE) (VS-Code + Code Runner Expansion + Python Extension)
    # IDLE: open console, set Debug to on, run line by line
    # Vs-Code works different

    # you can set breakpoints to let the debugger stop at that line of code (red dot next to line number)
    # or write a breakpoint: for x in range (1000):
    #                           #DO SOMETHING
    #                           if x = 500:
    #                               print ("breakpoint")
