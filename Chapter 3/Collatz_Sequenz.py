# if number even print number //2
# if number odd print number*3 +1
# user types integer and programm reruns until output = 1
# bonus: if input is not an int, remind the user


def collatz(number):
    if number %2 == 0:
        number = number // 2
    else:
        number = number*3 + 1
    return number

print ("Write a number to start the collatz sequenz")
while True:
    try:
        x = int(input())
    except:
        print ("Please Enter an Integer")
        continue
    break

while x != 1:
    x = collatz(x)
    print (x)