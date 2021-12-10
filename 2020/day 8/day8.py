data = []
with open('day8_input.txt') as file:
    data = [line.strip().split() for line in file]

# Make things integers for easier use
for i in range(len(data)):
    data[i][1] = int(data[i][1])
    data[i].append(0)

acc = 0
i = 0
while True:
    instruction = data[i][0]
    value = data[i][1]
    times_visited = data[i][2]

    if times_visited > 0:
        # We have visited this instruction already
        print(last)
        break
    else:
        # Specify that we have visited this instruction
        data[i][2] += 1

    if instruction == "nop":
        i += 1
    elif instruction == "acc":
        acc += value
        i += 1
    elif instruction == "jmp":
        i += value

print(acc)
