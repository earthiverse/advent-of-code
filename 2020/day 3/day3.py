map = []
with open('day3_input.txt') as file:
    map = file.read().splitlines()

num_trees = 0
offset = 0

for line in map:
    if(line[offset] == '#'):
        num_trees += 1
    
    offset = (offset + 3) % len(line)

print(num_trees)
