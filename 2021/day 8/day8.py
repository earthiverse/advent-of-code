data = []
with open('day8_input.csv') as file:
    while True:
        try:
            line = next(file).split('|')
            signals = line[0].split()
            outputs = line[1].split()
            data.append([signals, outputs])
        except StopIteration:
            break

all = 0
for [signals, outputs] in data:
    mapping = {"a": " ", "b": " ", "c": " ",
               "d": " ", "e": " ", "f": " ", "g": " "}

    # Determine the unique numbers (1, 7, 4, and 8)
    for signal in signals:
        if len(signal) == 2:
            # It's a 1
            one = set(signal)
        elif len(signal) == 3:
            # It's a 7
            seven = set(signal)
        elif len(signal) == 4:
            # It's a 4
            four = set(signal)
        elif len(signal) == 7:
            # It's an 8
            eight = set(signal)

    mapping["a"] = next(iter(seven - one))

    # Determine 3 and 6 by the # of segments and overlap with 1
    for signal in signals:
        potential = set(signal)

        if len(signal) == 5 and one.issubset(potential):
            three = potential
        elif len(signal) == 6 and not one.issubset(potential):
            six = potential

    mapping["c"] = next(iter(eight - six))
    mapping["g"] = next(iter(three - four - seven))

    # Determine 2 by the # of segments, not 3, and having segment 'c'
    for signal in signals:
        potential = set(signal)

        if len(signal) == 5 and mapping["c"] in potential and potential != three:
            two = potential

    mapping["f"] = next(iter(three - two))

    mapping["d"] = next(
        iter(three - set([mapping["a"], mapping["c"], mapping["f"], mapping["g"]])))
    mapping["b"] = next(iter(four - three))

    five = set([mapping["a"], mapping["b"],
               mapping["d"], mapping["f"], mapping["g"]])
    nine = set([mapping["a"], mapping["b"],
               mapping["c"], mapping["d"], mapping["f"], mapping["g"]])

    mapping["e"] = next(iter(eight - three - four))

    zero = set([mapping["a"], mapping["b"], mapping["c"],
               mapping["e"], mapping["f"], mapping["g"]])

    final = ""
    for output in outputs:
        potential = set(output)
        if potential == zero:
            final += "0"
        elif potential == one:
            final += "1"
        elif potential == two:
            final += "2"
        elif potential == three:
            final += "3"
        elif potential == four:
            final += "4"
        elif potential == five:
            final += "5"
        elif potential == six:
            final += "6"
        elif potential == seven:
            final += "7"
        elif potential == eight:
            final += "8"
        elif potential == nine:
            final += "9"

    print(outputs, int(final))
    all += int(final)

print("Total sum: {}".format(all))
