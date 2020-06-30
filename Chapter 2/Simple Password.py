import time
x = 0

print ("Please create an Account first")
time.sleep (3)
print ("")
print ("Enter your Account Name")
AccountName = input()
time.sleep (3)
print ("")
print ("Enter your Password")
AccountPassword = input()
print ("")

while True:
    print ("What's your name?")
    CheckName = input()
    if CheckName != AccountName:
        continue
    print ("Hello, "+ AccountName + " ! Enter your Password, please.")
    while True:
        print ("Enter Password")
        CheckPassword = input()
        if CheckPassword != AccountPassword:
            print ("Wrong, please try again")
            print ("")
            x = x+1
            if x >= 3:
                WaitingTime = 3*x
                print ("You have to wait " + str(WaitingTime) + " seconds to try again")
                time.sleep(3*x)
                print ("Try Again")
            continue
        break
    print ("Welcome, " + AccountName + " !")
    break
