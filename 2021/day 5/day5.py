data = []
maxX = 0
maxY = 0
with open('day5_input.csv') as file:
    for line in file.readlines():
        datum = line.split("->")
        
        fromDatum = list(map(int, datum[0].split(",")))
        if(fromDatum[0] > maxX):
            maxX = fromDatum[0]
        if(fromDatum[1] > maxY):
            maxY = fromDatum[1]
        toDatum = list(map(int, datum[1].split(",")))
        if(toDatum[0] > maxX):
            maxX = toDatum[0]
        if(toDatum[1] > maxY):
            maxY = toDatum[1]
        data.append([fromDatum, toDatum])

counts = [ [0] * (maxX + 1) for i in range(maxY + 1)]
for datum in data:
    fromDatum = datum[0]
    toDatum = datum[1]
    if fromDatum[0] == toDatum[0]:
        x = fromDatum[0]
        increment = 1
        if fromDatum[1] > toDatum[1]:
            increment = -1
        for y in range(fromDatum[1], toDatum[1] + increment, increment):
            counts[y][x] += 1
    elif fromDatum[1] == toDatum[1]:
        y = fromDatum[1]
        increment = 1
        if fromDatum[0] > toDatum[0]:
            increment = -1
        for x in range(fromDatum[0], toDatum[0] + increment, increment):
            counts[y][x] += 1

num2 = 0
for y in counts:
    for x in y:
        if x >= 2:
            num2 += 1

print("# points visited 2 or more times: {}".format(num2))

for datum in data:
    fromDatum = datum[0]
    toDatum = datum[1]
    if fromDatum[0] != toDatum[0] and fromDatum[1] != toDatum[1]:
        xIncrement = 1
        if fromDatum[0] > toDatum[0]:
            xIncrement = -1
        yIncrement = 1
        if fromDatum[1] > toDatum[1]:
            yIncrement = -1
        x = fromDatum[0]
        y = fromDatum[1]
        while x != (toDatum[0] + xIncrement) and y != (toDatum[1] + yIncrement):
            counts[y][x] += 1
            x += xIncrement
            y += yIncrement

num2 = 0
for y in counts:
    for x in y:
        if x >= 2:
            num2 += 1

print("# points visited 2 or more times (w/ diagonals): {}".format(num2))