import time, random, copy

height = 15
width = 40

#Create Initial 2D-Field in a list
field = [[] for i in range (height)]
for y in range(height):
    for x in range(width):
        starting_potitions = random.randint(0,1)
        if starting_potitions == 1:
            field[y].append("1 ")
        else:
            field[y].append("0 ")

current_field = copy.deepcopy(field)

while True:

    #Print the current Field
    for y in range(height):
        for x in range(width):
            print (current_field[y][x], end ="")
        print ("")

    # Determine wether object lives or dies
    field = copy.deepcopy(current_field)
    sorrounded_counter = 0


    for y in range(height):
        for x in range (width):
            top = (y-1) % height
            bottom = (y+1) % height
            left = (x-1) % width
            right = (x+1) % width

            if field[top][left] == "1 ":
                    sorrounded_counter += 1
            if field[top][x] == "1 ":
                    sorrounded_counter += 1
            if field[top][right] == "1 ":
                    sorrounded_counter += 1
            if field[y][left] == "1 ":
                    sorrounded_counter += 1
            if field[y][right] == "1 ":
                    sorrounded_counter += 1
            if field[bottom][left] == "1 ":
                    sorrounded_counter += 1
            if field[bottom][x] == "1 ":
                    sorrounded_counter += 1
            if field[bottom][right] == "1 ":
                    sorrounded_counter += 1

            if sorrounded_counter < 2 or sorrounded_counter > 3:
                current_field[y][x] = "0 "
            elif sorrounded_counter == 3:
                current_field[y][x] = "1 "
            else:
                current_field[y][x] = field[y][x]

            sorrounded_counter = 0

    input()