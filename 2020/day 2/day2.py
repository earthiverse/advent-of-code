import re
pattern = re.compile('^(\d+)-(\d+)\s+([a-zA-Z]):\s+(.+)$')

num_invalid = 0
num_valid = 0
with open('day2_input.txt') as file:
    for line in file:
        result = pattern.match(line)

        minimum = int(result.group(1))
        maximum = int(result.group(2))
        letter = result.group(3)
        password = result.group(4)

        count = password.count(letter)

        if (count < minimum) or (count > maximum):
            num_invalid += 1
        else:
            num_valid += 1

print(num_valid)
