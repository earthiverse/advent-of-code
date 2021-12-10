data = []
with open('day9_input.txt') as file:
    data = [int(line.strip()) for line in file]

preamble_length = 25

available_data = []
for i in range(preamble_length):
    available_data.append(data[i])

#print(available_data)

target = -1
for i in range(preamble_length, len(data)):
    current = data[i]

    can = False
    for j in range(len(available_data) - 1):
        for k in range(j + 1, len(available_data)):
            if available_data[j] + available_data[k] == current:
                can = True
                break

        if can:
            break

    if not can:
        target = current
        break

    #print(available_data)
    available_data.pop(0)
    available_data.append(current)

print("part 1:", target)

for i in range(len(data)):
    current_nums = [data[i]]
    for j in range(i + 1, len(data)):
        current_nums.append(data[j])
        if sum(current_nums) == target:
            print("part 2:", min(current_nums) + max(current_nums))
