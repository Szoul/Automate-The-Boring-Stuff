"""
22. How would you write a regex that matches a sentence where 
the first word is either Alice, Bob, or Carol; the second word 
is either eats, pets, or throws; the third word is apples, cats, 
or baseballs; and the sentence ends with a period? This regex 
should be case-insensitive. It must match the following:
"""
m1 ='Alice eats apples.'
m2 ='Bob pets cats.'
m3 ='Carol throws baseballs.'
m4 ='Alice throws Apples.'
m5 ='BOB EATS CATS.'
"""
but not the following:
"""
n1 ='RoboCop eats apples.'
n2 ='ALICE THROWS FOOTBALLS.'
n3 ='Carol eats 7 cats.'

import re

this_Regex = re.compile(r"(alice|bob|carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.", re.I)
test_list = [m1,m2,m3,m4,m5,n1,n2,n3]

for x in test_list:
    if this_Regex.search(x) is not None:
        print ((this_Regex.search(x)).group() + " --> Matched to regex")
    else:
        print (str(x) + " --> is not a viable match for the regex.")