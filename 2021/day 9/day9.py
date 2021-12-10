data = []
with open('day9_input.csv') as file:
    for line in file.read().splitlines():
        data.append(list(map(int, line)))

basins = []
for y in range(0, len(data)):
    basins.append([-1] * len(data[0]))


def populateBasin(x, y, value, basinName):
    if x < 0 or y < 0 or y >= len(data) or x >= len(data[0]):
        # Bounds check
        return

    basin = basins[y][x]
    if basin >= 0:
        # We already have a basin for this point
        return

    current = data[y][x]
    if current == 9:
        # It's a high point, not in any basin
        return
    if current < value:
        # It's
        return

    basins[y][x] = basinName

    populateBasin(x - 1, y, current, basinName)
    populateBasin(x + 1, y, current, basinName)
    populateBasin(x, y - 1, current, basinName)
    populateBasin(x, y + 1, current, basinName)
    # populateBasin(x + 1, y + 1, current, basinName)
    # populateBasin(x - 1, y + 1, current, basinName)
    # populateBasin(x + 1, y - 1, current, basinName)
    # populateBasin(x - 1, y - 1, current, basinName)


totalRisk = 0
b = 0
for y in range(0, len(data)):
    for x in range(0, len(data[0])):
        current = data[y][x]
        nearby = []
        try:
            nearby.append(data[y - 1][x])
        except:
            pass  # Do nothing
        try:
            nearby.append(data[y + 1][x])
        except:
            pass  # Do nothing
        try:
            nearby.append(data[y][x - 1])
        except:
            pass  # Do nothing
        try:
            nearby.append(data[y][x + 1])
        except:
            pass  # Do nothing

        if all(current < i for i in nearby):
            riskLevel = current + 1
            totalRisk += riskLevel
            populateBasin(x, y, current - 1, b)
            b += 1

print("Total Risk: {}".format(totalRisk))

basinSizes = []
for i in range(0, b + 1):
    count = 0
    for y in range(0, len(data)):
        for x in range(0, len(data[0])):
            current = basins[y][x]
            if current == i:
                count += 1
    basinSizes.append({"basin": i, "size": count})

basinSizes.sort(key=lambda x: x["size"], reverse=True)

prod = 1
for i in range(0, 3):
    prod *= basinSizes[i]["size"]
print("3 largest basins product: {}".format(prod))

# for basin in basins:
#     print(basin)
# print(basinSizes)
