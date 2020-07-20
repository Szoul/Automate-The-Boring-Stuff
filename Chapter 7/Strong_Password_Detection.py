#! python 3.8.3
#Strong_Password_Detection: Detect if a Password is strong enough (wow)

'''
Project description:
Write a function that uses regular expressions to make sure the password 
string it is passed is strong. A strong password is defined as one that is 
at least eight characters long, contains both uppercase and lowercase 
characters, and has at least one digit. You may need to test the string 
against multiple regex patterns to validate its strength.
'''

#at least 8 characters; both (at least) upper-and lowercase characters; at least one digit
#I assume that the only input is the unchecked-password (of any length)

def is_strong_password (password):
    import re

    is_strong = True

    upper_case_regex = re.compile(r"[A-Z]")
    has_upper_case = upper_case_regex.search(password)
    if has_upper_case == None:
        print ("This password is missing at least one upper-case-Letter")
        is_strong = False
    
    lower_case_regex = re.compile(r"[a-z]")
    has_lower_case = lower_case_regex.search(password)
    if has_lower_case == None:
        print ("This password is missing at least one lower-case-Letter")
        is_strong = False

    number_regex = re.compile(r"\d")
    has_digit = number_regex.search(password)
    if has_digit == None:
        print ("This password is missing at least one digit")
        is_strong = False
    
    lenght = len(password)
    if lenght < 8:
        print ("Your password isn't long enough. At least 8 characters are required.")
        is_strong = False
    
    if is_strong:
        print ("Your password: '"+ password + "'" + " is strong enough")
    
    return is_strong


strong_password = False
while not strong_password:
    print ("Enter a Password \n\n")
    password = input()
    strong_password = is_strong_password(password)