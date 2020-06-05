import time
empty_spaces = 0
indent_direction = "increasing"
stars = "***********"

for i in range (1000):
    time.sleep(0.05)
    print (" "*empty_spaces, end='')
    print (stars)
    if indent_direction == "increasing":
        empty_spaces +=1
        if empty_spaces == 50:
            indent_direction = "decreasing"
    elif indent_direction == "decreasing":
        empty_spaces -= 1
        if empty_spaces == 0:
            indent_direction = "increasing"
        