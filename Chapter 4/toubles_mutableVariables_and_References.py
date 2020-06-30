aString = "Hiho"
slicey = aString[:2]
tobl = (aString, 1, "hello", True, 0.5, slicey)
toblo = ("hi", )
print ("_________________")
print ((type(tobl)))
print (str(type(toblo)))
print ("_________________")
its_a_LIST = list(tobl)
print (its_a_LIST)
print (str(type(its_a_LIST)))
print ("_________________")
no_it_isnt = tuple(its_a_LIST)
print (no_it_isnt)
print (str(type(no_it_isnt)))
print ("_________________")
just_a_bit = no_it_isnt[:1]
just_a_bit = list(just_a_bit)
print (just_a_bit)

print ("_________________")
mutable_list = [1,2,3,4]
print ("first ID: " + str(id(mutable_list)))
a_copy = mutable_list
mutable_list[1] = "mutated or muted?"
print (a_copy)
print ("second ID: " + str(id(a_copy)))
print ("_________________")
not_mutable = "this is not mutable"
print (not_mutable + ". ID: " + str(id(not_mutable)))
not_mutable_copy = not_mutable
not_mutable = "but it can be replaced"
print (not_mutable_copy + ". ID: " + str(id(not_mutable_copy)))
print (not_mutable + ". ID: " + str(id(not_mutable)))


