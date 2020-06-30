x = 0
for x in range (5,10):              #set x to start of range loop value?
    print (x)
print ("First Loop")


for x in range (0,10,2):            #set it to 0; only count every 2nd number
                                    # (or skip 1 number in between)
    print (x)
print ("Second Loop")


for x in range (0,-5,2):            # doesnt print anything? but why not 0?
    print (x)
print ("Third Loop")


for x in range (0,-5,-1):           # set x to 0, count negative
    print (x)
print ("Fourth Loop")


#for x in range (0.0, 5.1, 1.0):    #doesnt work -> only integer
#    print (x)
for x in range (int(0.0), int(5.1), int(1.0)):
    print (x)
print ("Fifth Loop")
