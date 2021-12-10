data = []
with open('day1_input.csv') as file:
    for number in file:
        data.append(int(number))


for i in range(len(data)):
    for j in range(i + 1, len(data)):
        if data[i] + data[j] == 2020:
            print(data[i] * data[j])
        
