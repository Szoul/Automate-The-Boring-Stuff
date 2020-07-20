def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
       if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')

#with regex matching method:
import re

def isPhoneNumber2 (text):
    phoneNumRegex = re.compile(r"\d{3}-\d{3}-\d\d\d\d")       #\d == a digit character
    match = phoneNumRegex.search(text)
    if match == None:
        return False
    else:
        print("Phone number found: " + match.group())

print(isPhoneNumber2(message))          #seems to only store the first viable match; need loop around the .search function for every match - how to?

'''
    1. Import the regex module with import re.
    2. Create a Regex object with the re.compile() function. (Remember to use a raw string.)
    3. Pass the string you want to search into the Regex object’s search() method. This returns a Match object.
    4. Call the Match object’s group() method to return a string of the actual matched text.
    4.2 findall() instead of search() will return all possible matches as a list (or touples in a list if there are groups)
    # https://pythex.org/  <-- tipps, expressions, testing
'''

phoneNumRegex2 = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex2.search('My phone number is (415) 555-4242.')
print (mo.groups())
print (mo.group(1))

print ("\n\n\n")

fruitmessage = "The pineapple hangs from the apple-tree inside a melongarden"
fruitRegex = re.compile(r"(pine)(apple)|(apple)|(melon)")

f_mo = fruitRegex.search(fruitmessage)
print (f_mo.group())
print (f_mo.groups())
print (fruitRegex.findall(fruitmessage))

# (searched segment in parantheses to mark it as a group) [addition]
#  ? == use it if its thee otherwise ignore it
#  [word one]|[word two] == either one of the words, whatever matches first
#  * == same as ?, but if it appeas more than 1 times at that potition count all instances
#  {[number],[optional number]}  -> only if previous segment appears [number] times OR betweeen [number] and [optional number] times
#  + == same as *, but it wont match if the previous segment doesnt exist at least 1 times
#  greedy matching: if possible it will always match the biggest possible group
#  non-greedy: add a ? to let it match the smallest possible group
#  MAKE OWN CHARACTER CLASS: r'[any character/number/marking...] ||| r"[^1] == anything but 1
#  MORE: on chapter 7 or pythex
 



