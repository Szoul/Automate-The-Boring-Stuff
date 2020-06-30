aString = "Hiho"
slicey = aString[:2]
tobl = (aString, 1, "hello", True, 0.5, slicey)
toblo = ("hi", )

print (str(type(tobl)))
print (str(type(toblo)))

its_a_LIST = list(tobl)
print (its_a_LIST)
print (str(type(its_a_LIST)))

no_it_isnt = tuple(its_a_LIST)
print (no_it_isnt)
print (str(type(no_it_isnt)))

just_a_bit = no_it_isnt[:1]
just_a_bit = list(just_a_bit)
print (just_a_bit)


mutable_list = [1,2,3,4]
print ("first ID: " + str(id(mutable_list)))
a_copy = mutable_list
mutable_list[1] = "mutated or muted?"
print (a_copy)
print ("second ID: " + str(id(a_copy)))

not_mutable = "this is not mutable"
print (not_mutable + ". ID: " + str(id(not_mutable)))
not_mutable_copy = not_mutable
not_mutable = "but it can be replaced"
print (not_mutable_copy + ". ID: " + str(id(not_mutable_copy)))
print (not_mutable + ". ID: " + str(id(not_mutable)))

def add_hi_to_list (hi):
    hi.append("hi")

print (its_a_LIST)
add_hi_to_list(its_a_LIST)
print (its_a_LIST)

import copy

its_a_different_List = copy.copy(its_a_LIST)
print ("ID of its_a_list: " + str(id(its_a_LIST)))
print ("ID of its_a_different_list: " + str(id(its_a_different_List)))
