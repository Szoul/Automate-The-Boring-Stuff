grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

#Think of grid[x][y] as being the character at the x- and y-coordinates of a “picture” drawn with
#text characters. The (0, 0) origin is in the upper-left corner, the x-coordinates increase going right,
#and the y-coordinates increase going down.
#Copy the previous grid value, and write code that uses it to print the image.

#printed top down (first list in grid == first printed line)
for y in range (len(grid)):
    for x in range (len(grid[y])):
        print (grid[y][x], end="")
    print ("")

print ("\n\n\n")

#printed left to right (first item of each list in grid == first printed line)
for y in range (len(grid[0])):
    for x in range (len(grid)):
        print (grid[x][y], end="")
    print ("")