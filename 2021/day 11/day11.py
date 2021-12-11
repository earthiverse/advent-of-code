data = []
with open('day11_input.csv') as file:
    for line in file.read().splitlines():
        datum = []
        for char in line:
            datum.append(int(char))
        data.append(datum)

for datum in data:
    print(datum)
print("Starting...")

numFlashesAll = 0
for i in range(1, 1001):
    ySize = len(data)
    xSize = len(data[0])

    # Increase all by 1
    for y in range(0, ySize):
        for x in range(0, xSize):
            data[y][x] += 1

    # Compute flashes
    y = -1
    while y < ySize - 1:
        y += 1
        x = -1
        while x < xSize - 1:
            x += 1
            value = data[y][x]

            if value == "X":
                # Already lit
                continue

            if value >= 10:
                data[y][x] = "X"

                for y2 in range(y - 1, y + 2):
                    for x2 in range(x - 1, x + 2):
                        if y2 < 0 or x2 < 0 or y2 >= ySize or x2 >= xSize:
                            # Out of bounds
                            continue

                        value2 = data[y2][x2]

                        if value2 == "X":
                            continue
                        else:
                            # Increase values around
                            data[y2][x2] += 1

                # Repeat search
                y = 0
                x = -1

    # Deal with flashes
    numFlashesStep = 0
    for y in range(0, ySize):
        for x in range(0, xSize):
            value = data[y][x]

            if value == "X":
                numFlashesStep += 1
                data[y][x] = 0

    inSync = True
    check = data[y][x]
    for y in range(0, ySize):
        if not inSync:
            break
        for x in range(0, xSize):
            if data[y][x] != check:
                inSync = False
                break
    if inSync:
        print("We are in sync on step {}!".format(i))
        break

    # Count flashes
    numFlashesAll += numFlashesStep
    # for datum in data:
    #     print(datum)
    print("Step {}, # Flashes: {}, # Flashes Total: {}".format(
          i, numFlashesStep, numFlashesAll))
