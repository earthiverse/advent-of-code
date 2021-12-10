data = []
with open('day6_input.txt') as file:
    data = file.read().splitlines()

answers = {}
lengths = []
for datum in data:
    if(datum == ''):
        lengths.append(len(answers))
        answers = {}
    else:
        for answer in datum:
            answers[answer] = True

lengths.append(len(answers))

print(sum(lengths))
