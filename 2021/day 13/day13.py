import re

grid = [["."]]
dots = []
folds = []
with open('day13_input.csv') as file:
    # Read points
    line = file.readline()
    maxX = 0
    maxY = 0
    while line != "":
        [x, y] = list(map(int,line.split(",")))

        if x > maxX:
            maxX = x
        if y > maxY:
            maxY = y

        dots.append([x, y])
        line = file.readline().strip()

    print("Grid is {} rows and {} columns".format(maxY + 1, maxX + 1))
    grid = [[ "." for x in range(0,maxX + 1)] for y in range(0,maxY + 1)]

    for dot in dots:
        [x, y] = dot
        grid[y][x] = "#"
    
    line = file.readline().strip()
    pattern = re.compile("^fold along (.)=(\d+)$")
    while line:
        result = pattern.match(line)

        axis = result.group(1)
        amount = int(result.group(2))
        folds.append([axis, amount])
        line = file.readline().strip()
    
def foldX(xLine):
    global grid
    # print("folding x at col {}".format(xLine))

    foldLeft = xLine - 1
    foldRight = xLine + 1
    while foldLeft >= 0 and foldRight <= len(grid[0]):
        for y in range(0, len(grid)):
            valueLeft = grid[y][foldLeft]
            valueRight = grid[y][foldRight]

            if valueLeft == "#":
                grid[y][foldRight] = "#"
            if valueRight == "#":
                grid[y][foldLeft] = "#"

        foldLeft -= 1
        foldRight += 1
    
    # TODO: fold
    newGrid = []
    
    for y in range(len(grid)):
        newGrid.append(grid[y][0:xLine])
    
    grid = newGrid

def foldY(yLine):
    global grid
    # print("folding y at row {}".format(yLine))

    foldUpper = yLine - 1
    foldLower = yLine + 1
    while foldUpper >= 0 and foldLower <= len(grid) - 1:
        # print("Combining lines {} and {}".format(foldUpper, foldLower))
        lineUpper = grid[foldUpper]
        lineLower = grid[foldLower]
        for x in range(0, len(lineLower)):
            upper = lineUpper[x]
            lower = lineLower[x]
            if lower == "#":
                lineUpper[x] = "#"
            if upper == "#":
                lineLower[x] = "#"
        
        foldUpper -= 1
        foldLower += 1
    
    grid = grid[0: yLine]

def countDots():
    global grid

    count = 0
    for y in range(0, len(grid)):
        for x in range(0, len(grid[0])):
            if grid[y][x] == "#":
                count += 1
    
    return count

print("# Dots @ Step # 0: {}".format(countDots()))
for i in range(0, len(folds)):
    [axis, amount] = folds[i]
    if axis == "x":
        foldX(amount)
    elif axis == "y":
        foldY(amount)
    print("# Dots @ Step # {}: {}".format(i + 1, countDots()))

for line in grid:
    print(line)