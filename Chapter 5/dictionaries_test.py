dic = {"name":"Tom", "age":"24"}
print(dic["name"])

dic2 = {"age":"24", "name":"Tom"}
if dic == dic2:
    print ("dictionaries have no order")

if "age" in dic and "name" in dic2:
    print (dic["age"] + " is the age of " + dic2["name"])

print (dic)

secondname = input("whats his second name?")
dic["secondname"] = secondname

print (dic)

print ("_________________________________")

for x in dic.keys():                #for loop iterates over every item in dictionary
    print (x)                       #dictionary{key:value} = dictionary{item}
for i in dic.values():
    print (i)
for y in dic.items():
    print (y)

print ("___________________________________")

print (dic.keys())                  #touple
dic_keylist = list(dic.keys())      #changed to list
print (dic_keylist)

print ("_____________________________")

print (dic.get("name",0))
print (dic.get("thisdoesnotexist",0))   #.get(key,alternative) returns the value belonging to the key OR the second value if the key does not exist
dic.setdefault("thisdoesnotexist","now it does")        #.setdefault(key,value) : if the key doesnt exist yet create it and give it the value
print(dic.get("thisdoesnotexist",0))

print ("_______________________________")

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)               #checks if key exists / creates it if it doesnt                                  
    count[character] = count[character] + 1      #adds 1 to the count of the key

print(count)                                     #prints each key and how often it appeared in the text