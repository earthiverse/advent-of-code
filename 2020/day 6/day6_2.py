data = []
with open('day6_input.txt') as file:
    data = file.read().splitlines()

answers = {}
num_people = 0
lengths = []
for datum in data:
    if(datum == ''):
        length = 0
        for answer in answers:
            if(answers[answer] == num_people):
                length += 1
        lengths.append(length)
        answers = {}
        num_people = 0
    else:
        num_people += 1
        for answer in datum:
            if answer in answers:
                answers[answer] += 1
            else:
                answers[answer] = 1

print(sum(lengths))
