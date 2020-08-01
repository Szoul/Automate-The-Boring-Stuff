hello = "Hello, World!"

for i in range (len(hello)):
    if "l" in hello[i:i+3]:
        print (hello[-20:20])                     # why does this work?/why isn't it out of range?
        print (hello[i:i+3])                      # if "out of range" it just stops at end of string


    # --> stackoverflow (9490058)

'''
Given a slice expression like s[i:j:k], (k = 1 if not specified)

    The slice of s from i to j with step k is defined as the sequence of 
    items with index x = i + n*k such that 0 <= n < (j-i)/k. In other words, 
    the indices are i, i+k, i+2*k, i+3*k and so on, stopping when j is reached 
    (but never including j). When k is positive, i and j are reduced to len(s) 
    if they are greater
''' 
    # --> for some reason instead of making an error for out of index, it just adjusts the index to max (if positive)/min (if negative) length of splice
    # hello[-20:20] == hello [:len(hello)]            
    # hello [i:i+3] == hello [i:] if i+3 > len(hello)
    # BUT:

print ("\n\n")
print (hello[:len(hello)])

if hello[:] == hello [-5:20]:
    print ("well")                              # doesn't print --> it is not the "same" even if output looks the same
if hello[1] == hello [1:2]:
    print ("well2")                             # does print, but it cannot be the "same" since...

print ("\n\n")
try:
    print (hello[20:21] + "...")                # this prints even though hello [20:21] is empty
    print (hello [20])                          # this gives an Index-Error, because hello [20] doesn't exist
except IndexError:
    print ("well3")

# more explaination: stackoverflow (22951107)
'''
Slicing is used to create a new list. If the indices don't fall within the 
range of the number of elements in the list, we can return an empty list. So, 
we don't have to throw an error.
But, if we try to access the elements in the list which is greater 
than the number of elements, we cannot return any default value (not even None 
because it could be a valid value in the list). That is why

IndexError: list index out of range

is thrown.
'''

slice1 = hello [:]          # though: the "endproduct" of a slice is not a list; it is a string (in this case)

if slice1 == str(slice1):
    print ("well4")