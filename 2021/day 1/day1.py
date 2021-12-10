data = []
with open('day1_input.csv') as file:
    for number in file:
        data.append(int(number))

last = data[0]
numIncreases = 0
for i in range(1, len(data)):
    current = data[i]
    if(current > last):
        numIncreases += 1
    last = current

print("# Increases: {}".format(numIncreases))

interval = [data[0], data[1], data[2]]
last = sum(interval)
numIncreases = 0
for i in range(3, len(data)):
    interval[i % 3] = data[i]
    current = sum(interval)
    if(current > last):
        numIncreases += 1
    last = current

print("# Increases (three-measurement sliding window): {}".format(numIncreases))