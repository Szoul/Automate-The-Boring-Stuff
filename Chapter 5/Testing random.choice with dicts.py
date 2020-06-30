import random

dic = {"integer": 1, "string": "hi", "boolean": True, "float": 1.0}

print ("randomkey:")
randomkey = random.choice(list(dic.keys()))
print (randomkey)

print ("\n" + "randomvalue:")
randomvalue = random.choice(list(dic.values()))
print (randomvalue)

print ("\n" + "randomitem")
randomitem = random.choice(list(dic.items()))
print (randomitem)