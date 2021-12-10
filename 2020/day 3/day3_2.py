map = []
with open('day3_input.txt') as file:
    map = file.read().splitlines()

width = len(map[0])

# Right 1, Down 1
num_trees_1 = 0
offset_1 = 0
for i in range(len(map)):
    if(map[i][offset_1] == '#'):
        num_trees_1 += 1
    
    offset_1 = (offset_1 + 1) % width
    
# Right 3, Down 1
num_trees_2 = 0
offset_2 = 0
for i in range(len(map)):
    if(map[i][offset_2] == '#'):
        num_trees_2 += 1
    
    offset_2 = (offset_2 + 3) % width

# Right 5, Down 1
num_trees_3 = 0
offset_3 = 0
for i in range(len(map)):
    if(map[i][offset_3] == '#'):
        num_trees_3 += 1
    
    offset_3 = (offset_3 + 5) % width

# Right 7, Down 1
num_trees_4 = 0
offset_4 = 0
for i in range(len(map)):
    if(map[i][offset_4] == '#'):
        num_trees_4 += 1
    
    offset_4 = (offset_4 + 7) % width

# Right 1, Down 2
num_trees_5 = 0
offset_5 = 0
for i in range(0, len(map), 2):
    if(map[i][offset_5] == '#'):
        num_trees_5 += 1
    
    offset_5 = (offset_5 + 1) % width

print(num_trees_1, num_trees_2, num_trees_3, num_trees_4, num_trees_5)
print(num_trees_1 * num_trees_2 * num_trees_3 * num_trees_4 * num_trees_5)
