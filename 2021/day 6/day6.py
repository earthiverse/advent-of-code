fish = [0, 0, 0, 0, 0, 0, 0, 0, 0]
with open("day6_input.csv") as file:
    for f in list(map(int, file.readline().split(","))):
        fish[f] += 1

print(fish)

for day in range(0, 256):
    tempFish = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(0, 9):
        f = fish[i]
        if(i == 0):
            tempFish[6] += f
            tempFish[8] += f
        else:
            tempFish[i - 1] += f
    fish = tempFish
    print("Num Day {}: {}".format(day + 1, sum(fish)))
