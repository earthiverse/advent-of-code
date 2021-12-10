import re

data = []
with open('day7_input.txt') as file:
    data = file.read().splitlines()

pattern = re.compile("(.+?) bags contain (.+?)\.")
pattern_2 = re.compile("(\d+) (.+?) bags?")

bags = {}
for datum in data:
    match = pattern.match(datum)

    outer_bag = match.group(1)
    bags[outer_bag] = {}
    for inner_bag in match.group(2).split(','):
        inner_bag = inner_bag.strip()

        match_2 = pattern_2.match(inner_bag)
        if match_2:
            bags[outer_bag][match_2.group(2)] = match_2.group(1)

explored_types = set()
types = {"shiny gold"}
while len(types) > 0:
    to_explore = types.pop()

    for bag in bags:
        if to_explore in bags[bag] and to_explore not in explored_types:
            types.add(bag)
    
    explored_types.add(to_explore)

print(len(explored_types) - 1)
