dict1 = {"key1":"value1", "key1":"value2"}
dict2 = {1:1,1:2}

for x in range(0):
    print (dict1)
    print (dict1.get("key1"))
    print (dict2)
    print (dict2.get(1))

list1 = list(dict1.items())
print (list1)

if "value1" in dict1.values():
    print ("value1")
else:
    print ("not value 1")

#Python doesnt support duplicate keys in a dictionary
#it seems like the two keys of the same name and its value is overwritte by the second one
# Workaround: use a single key and as a value make a list of all the items belonging there
#for example:

dict1 = {"key1":["value1","value2"]}


