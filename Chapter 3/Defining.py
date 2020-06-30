def emptyprint(number_of_empty_lines):
    for _ in range (number_of_empty_lines):                 # why desnt it work like outside defining a function?  | for i in range(10):
                                                            # the "i" is an unused variable inside this definition |     print ("")
        print()

print ("hi")
number_of_empty_lines = int(input())
emptyprint(number_of_empty_lines)
print("worked")
input()


y = int(input())
for x in range (y):
    print ("")