import sys

crabs = []
with open('day7_input.csv') as file:
    crabs = list(map(int, file.readline().split(",")))

minPosition = min(crabs)
maxPosition = max(crabs)
costs = {i: 0 for i in range(minPosition, maxPosition + 1)}

for crab in crabs:
    for position in costs:
        cost = abs(position - crab)
        costs[position] += cost

bestPosition = -sys.maxsize - 1
bestCost = sys.maxsize
for position in costs:
    cost = costs[position]
    if(cost < bestCost):
        bestCost = cost
        bestPosition = position

print("#1: Best is to move to {} at a cost of {}".format(bestPosition, bestCost))

costs = {i: 0 for i in range(minPosition, maxPosition + 1)}
fuelUsages = {0: 0}
for i in range(1, 1 + maxPosition - minPosition):
    fuelUsages[i] = fuelUsages[i - 1] + i

for crab in crabs:
    for position in costs:
        cost = fuelUsages[abs(position - crab)]
        costs[position] += cost

minPosition = -sys.maxsize - 1
minCost = sys.maxsize
for position in costs:
    cost = costs[position]
    if(cost < minCost):
        minCost = cost
        minPosition = position

print("#2: Best is to move to {} at a cost of {}".format(minPosition, minCost))
