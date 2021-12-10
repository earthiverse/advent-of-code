data = []
with open('day10_input.txt') as file:
    data = [int(line.strip()) for line in file]

data.append(0)
data.append(max(data) + 3)

data.sort()

print(data)

num_choice = 1
i = 0
while i < len(data):
    this_datum = data[i]

    # Find out how long the run of 1s is
    temp = this_datum
    run_length = 1
    for j in range(i + 1, len(data)):
        if data[j] == temp + 3:
            i = j - 1
            break
        elif data[j] == temp + 1:
            run_length += 1
        temp = data[j]

    #print(run_length)
    if run_length == 3:
        num_choice *= 2
    elif run_length == 4:
        num_choice *= 4
    elif run_length == 5:
        num_choice *= 7

    i += 1
        
print(num_choice)
