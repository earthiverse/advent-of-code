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
            bags[outer_bag][match_2.group(2)] = int(match_2.group(1))

print(bags)

def count_bags(color):
    count = 1
    for bag in bags[color]:
        count += bags[color][bag] * count_bags(bag)
    return count

print(count_bags("shiny gold") - 1)
