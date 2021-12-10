data = []
with open('day10_input.csv') as file:
    data = file.read().splitlines()

corruptScore = 0
incompleteScores = []
for datum in data:
    stack = []
    corrupt = False

    for i in range(0, len(datum)):
        char = datum[i]
        if char in "{([<":
            stack.append(char)
        elif char == "}":
            if stack[-1] == "{":
                stack.pop()
            else:
                corrupt = True
                corruptScore += 1197
                break
        elif char == ")":
            if stack[-1] == "(":
                stack.pop()
            else:
                corrupt = True
                corruptScore += 3
                break
        elif char == "]":
            if stack[-1] == "[":
                stack.pop()
            else:
                corrupt = True
                corruptScore += 57
                break
        elif char == ">":
            if stack[-1] == "<":
                stack.pop()
            else:
                corrupt = True
                corruptScore += 25137
                break

    if corrupt:
        pass
        #print("{} is corrupt at {}".format(datum, i))
    else:
        incompleteScore = 0
        stack.reverse()
        for char in stack:
            incompleteScore *= 5
            if char == "{":
                incompleteScore += 3
            elif char == "[":
                incompleteScore += 2
            elif char == "<":
                incompleteScore += 4
            elif char == "(":
                incompleteScore += 1
        incompleteScores.append(incompleteScore)

incompleteScores.sort()
print("Corrupt Score: {}".format(corruptScore))
print("Middle Score: {}".format(
    incompleteScores[(len(incompleteScores)-1)//2]))
