import re
pattern = re.compile('^(\d+)-(\d+)\s+([a-zA-Z]):\s+(.+)$')

num_invalid = 0
num_valid = 0
with open('day2_input.txt') as file:
    for line in file:
        result = pattern.match(line)

        pos_1 = int(result.group(1))
        pos_2 = int(result.group(2))
        letter = result.group(3)
        password = result.group(4)

        letter_1 = password[pos_1 - 1]
        letter_2 = password[pos_2 - 1]

        if (letter_1 == letter):
            if(letter_2 != letter):
                num_valid += 1
            else:
                num_invalid += 1
        else:
            if(letter_2 == letter):
                num_valid += 1
            else:
                num_invalid += 1

print(num_valid)
