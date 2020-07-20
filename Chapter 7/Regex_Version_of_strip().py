#! python 3.8.3
#Regex_Version_of_strip().py: imitate the strip() function including a regex

'''
Project description:
Write a function that takes a string and does the same thing as the strip() 
string method. If no other arguments are passed other than the string to strip, 
then whitespace characters will be removed from the beginning and end of the 
string. Otherwise, the characters specified in the second argument to the function 
will be removed from the string.
'''
# strip([text], [characters to be removed]) > if no 2nd argument, remove whitespace 

#regex to detect whitespace(\s)
#replace (regex.sub([substitute],[text])) (substitute = "replace with nothing")

def regex_strip (text, remove_text="\s*"):

    

    import re
    start_regex = re.compile(rf"^{remove_text}")
    end_regex = re.compile(rf"{remove_text}$")
    text = start_regex.sub("", text)
    text = end_regex.sub("", text)

    return text

test_text = "\n\nEine Kugel läuft um die Ecke und fällt um.          "

#regex_strip(text, remove_text) seems to work the same way as text.strip(remove_text)
print ("..." + test_text + "\n_______________________________________________")
print ("__" + test_text.strip("\n\nEine") + "__")
print ("\n\n")
print ("__" + regex_strip(test_text, "\n\nEine") + "__")
print ("\n_______________________________________________\n")
print ("__" + test_text.strip() + "__")
print ("\n\n")
print ("__" + regex_strip(test_text) + "__")