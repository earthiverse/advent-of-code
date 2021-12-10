import copy

data = []
with open('day8_input.txt') as file:
    data = [line.strip().split() for line in file]

# Make things integers for easier use
for i in range(len(data)):
    data[i][1] = int(data[i][1])
    data[i].append(0)

def hasLoop(d):
    i = 0
    while True:
        if i >= len(d):
            # No loop!
            return False
        
        instruction = d[i][0]
        value = d[i][1]
        times_visited = d[i][2]

        if times_visited > 0:
            # We have visited this instruction already
            return True
        else:
            # Specify that we have visited this instruction
            d[i][2] += 1

        if instruction == "nop":
            i += 1
        elif instruction == "acc":
            i += 1
        elif instruction == "jmp":
            i += value

def getAcc(d):
    acc = 0
    i = 0
    while True:
        if i >= len(d):
            return acc
        
        instruction = d[i][0]
        value = d[i][1]

        if instruction == "nop":
            i += 1
        elif instruction == "acc":
            acc += value
            i += 1
        elif instruction == "jmp":
            i += value

for i in range(len(data)):
    instruction = data[i][0]

    if instruction == "jmp":
        newData = copy.deepcopy(data)
        newData[i][0] = "nop"
        if not hasLoop(newData):
            print(getAcc(newData))
            break
    elif instruction == "nop":
        newData = copy.deepcopy(data)
        newData[i][0] = "jmp"
        if not hasLoop(newData):
            print(getAcc(newData))
            break
