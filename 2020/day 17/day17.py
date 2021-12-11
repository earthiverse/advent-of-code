state3D = []
state4D = []
with open('day17_sample_input.csv') as file:
    input3D = []
    input4D = []
    for line in file.read().splitlines():
        input3D.append(list(line))

    ySize = len(input3D)
    xSize = len(input3D[0])

    state3D.append(([["."] * xSize]) * ySize)
    state3D.append(input3D)
    state3D.append(([["."] * xSize]) * ySize)


def enlarge3D(input):
    zSize = len(input)
    ySize = len(input[0])
    xSize = len(input[0][0])

    print(zSize, ySize, xSize)

    # Make the array for the output, grown in size
    output = [[["." for x in range(xSize + 2)]
               for y in range(ySize + 2)] for z in range(zSize + 2)]

    # Copy the state in to the middle of the
    for z in range(0, zSize):
        for y in range(0, ySize):
            for x in range(0, xSize):
                output[z + 1][y + 1][x + 1] = input[z][y][x]

    return output


def enlarge4D(input):
    zzSize = len(input)
    zSize = len(input[0])
    ySize = len(input[0][0])
    xSize = len(input[0][0][0])

    print(zzSize, zSize, ySize, xSize)

    # Make the array for the output, grown in size
    output = [[[["." for x in range(xSize + 2)]
               for y in range(ySize + 2)] for z in range(zSize + 2)] for zz in range(zzSize + 2)]

    # Copy the state in to the middle of the
    for zz in range(0, zzSize):
        for z in range(0, zSize):
            for y in range(0, ySize):
                for x in range(0, xSize):
                    output[zz + 1][z + 1][y + 1][x + 1] = input[zz][z][y][x]

    return output


def compute3D(input):
    zSize = len(input)
    ySize = len(input[0])
    xSize = len(input[0][0])

    output = [[["." for z in range(xSize + 2)]
               for y in range(ySize + 2)] for x in range(zSize + 2)]

    for z in range(0, zSize):
        for y in range(0, ySize):
            for x in range(0, xSize):
                cell = input[z][y][x]

                # Let's check its neighbors
                numNeighbors = 0
                for z2 in range(z - 1, z + 2):
                    for y2 in range(y - 1, y + 2):
                        for x2 in range(x - 1, x + 2):
                            if x2 >= xSize or y2 >= ySize or z2 >= zSize or x2 < 0 or y2 < 0 or z2 < 0:
                                # Out of bounds
                                continue
                            if z2 == z and y2 == y and x2 == x:
                                # Don't calculate the center cell
                                continue

                            neighbor = input[z2][y2][x2]
                            if neighbor == "#":
                                numNeighbors += 1

                if cell == "#" and (numNeighbors == 2 or numNeighbors == 3):
                    output[z][y][x] = "#"
                elif cell == "." and numNeighbors == 3:
                    output[z][y][x] = "#"

    return output


def compute4D(input):
    zzSize = len(input)
    zSize = len(input[0])
    ySize = len(input[0][0])
    xSize = len(input[0][0][0])

    output = [[[["." for x in range(xSize + 2)]
               for y in range(ySize + 2)] for z in range(zSize + 2)] for zz in range(zzSize + 2)]

    for zz in range(0, zzSize):
        for z in range(0, zSize):
            for y in range(0, ySize):
                for x in range(0, xSize):
                    cell = input[zz][z][y][x]

                    # Let's check its neighbors
                    numNeighbors = 0
                    for zz2 in range(zz - 1, zz + 2):
                        for z2 in range(z - 1, z + 2):
                            for y2 in range(y - 1, y + 2):
                                for x2 in range(x - 1, x + 2):
                                    if x2 >= xSize or y2 >= ySize or z2 >= zSize or x2 < 0 or y2 < 0 or z2 < 0:
                                        # Out of bounds
                                        continue
                                    if z2 == z and y2 == y and x2 == x:
                                        # Don't calculate the center cell
                                        continue

                                    neighbor = input[zz2][z2][y2][x2]
                                    if neighbor == "#":
                                        numNeighbors += 1

                        if cell == "#" and (numNeighbors == 2 or numNeighbors == 3):
                            output[zz][z][y][x] = "#"
                        elif cell == "." and numNeighbors == 3:
                            output[zz][z][y][x] = "#"

    return output


def countActive3D(input):
    zSize = len(input)
    ySize = len(input[0])
    xSize = len(input[0][0])

    count = 0
    for z in range(0, zSize):
        for y in range(0, ySize):
            for x in range(0, xSize):
                cell = input[z][y][x]

                if cell == "#":
                    count += 1

    return count


def countActive4D(input):
    zzSize = len(input)
    zSize = len(input[0])
    ySize = len(input[0][0])
    xSize = len(input[0][0][0])

    count = 0
    for zz in range(0, zzSize):
        for z in range(0, zSize):
            for y in range(0, ySize):
                for x in range(0, xSize):
                    cell = input[zz][z][y][x]

                    if cell == "#":
                        count += 1

    return count


for i in range(0, 6):
    print("Cycle #{}".format(i + 1))
    state3D = enlarge3D(state3D)
    state3D = compute3D(state3D)
    print("Num Active: {}".format(countActive3D(state3D)))
