data = []
with open('day10_input.txt') as file:
    data = [int(line.strip()) for line in file]

data.sort()

#print(data)

last = 0
num_1 = 0
num_2 = 0
num_3 = 1 # 1 due to our device having +3 to highest
for i in range(0, len(data)):
    this = data[i]

    if this - last == 1:
        num_1 += 1
    elif this - last == 2:
        num_2 += 1
    elif this - last == 3:
        num_3 += 1

    last = this

print(num_1, num_2, num_3)
print(num_1 * num_3)
