state = []
with open('day17_sample_input.csv') as file:
    input = []
    for line in file.read().splitlines():
        input.append(list(line))

    yOrig = len(input)
    xOrig = len(input)

    state.append(([["."] * yOrig]) * xOrig)
    state.append(input)
    state.append(([["."] * yOrig]) * xOrig)


def enlarge(input):
    zSize = len(input)
    ySize = len(input[0])
    xSize = len(input[0][0])

    # Make the array for the output, grown in size
    output = [[["." for z in range(zSize + 2)]
               for y in range(ySize + 2)] for x in range(xSize + 2)]

    # Copy the state in to the middle of the
    for z in range(0, zSize):
        for y in range(0, ySize):
            for x in range(0, xSize):
                output[z + 1][y + 1][x + 1] = state[z][y][x]

    return output


def compute(input):
    zSize = len(input)
    ySize = len(input[0])
    xSize = len(input[0][0])

    output = [[["." for z in range(zSize + 2)]
               for y in range(ySize + 2)] for x in range(xSize + 2)]

    for z in range(0, zSize):
        for y in range(0, ySize):
            for x in range(0, xSize):
                cell = state[z][y][x]

                # Let's check its neighbors
                for dz in range(z - 1, z + 2):
                    for dy in range(y - 1, y + 2):
                        for dx in range(x - 1, x + 2):
                            if dz == z and dy == y and dx == x:
                                # Don't calculate the center cell
                                continue


print(state)
print("then")
print(enlarge(state))
