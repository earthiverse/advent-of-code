data = []
with open('day2_input.csv') as file:
    for line in file.read().splitlines():
        split = line.split()
        data.append([split[0], int(split[1])])

horiz = 0
depth = 0
for [command, amount] in data:
    match command:
        case "forward":
            horiz += amount
        case "down":
            depth += amount
        case "up":
            depth -= amount

print("Depth * Horizontal: {}".format(horiz * depth))

horiz = 0
depth = 0
aim = 0
for [command, amount] in data:
    match command:
        case "forward":
            horiz += amount
            depth += aim * amount
        case "down":
            aim += amount
        case "up":
            aim -= amount

print("Depth * Horizontal (with aim): {}".format(horiz * depth))