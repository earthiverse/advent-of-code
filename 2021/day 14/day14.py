import sys

templates = {}
with open("day14_input.csv") as file:
    # Read points
    polymer = file.readline().strip()

    for line in file.readlines():
        line = line.strip()
        if not line:
            continue
        [f, t] = line.split(" -> ")
        templates[f] = t

print("Templates:", templates)

segments = {}
pos = 0
while pos < len(polymer) - 1:
    segment = polymer[pos : pos + 2]
    if segment not in segments:
        segments[segment] = 1
    else:
        segments[segment] += 1
    pos += 1

print("Segments:", segments)
for i in range(0, 40):
    newSegments = {}
    for segment in segments:
        count = segments[segment]
        # The segment will split in to two new segments
        toAdd1 = segment[0] + templates[segment]
        if toAdd1 not in newSegments:
            newSegments[toAdd1] = count
        else:
            newSegments[toAdd1] += count

        toAdd2 = templates[segment] + segment[1]
        if toAdd2 not in newSegments:
            newSegments[toAdd2] = count
        else:
            newSegments[toAdd2] += count
    segments = newSegments

    maxValue = -sys.maxsize - 1
    minValue = sys.maxsize
    counts = {polymer[0]: 0.5, polymer[-1]: 0.5}
    for segment in newSegments:
        count = newSegments[segment]

        for letter in segment:
            if letter in counts:
                counts[letter] += count / 2
            else:
                counts[letter] = count / 2

    maxValue = -sys.maxsize - 1
    minValue = sys.maxsize
    for letter in counts:
        count = counts[letter]
        if count > maxValue:
            maxValue = count
        if count < minValue:
            minValue = count

    print("Stage {}".format(i + 1))
    print("  Segments: ", segments)
    print("  Counts: ", counts)
    print("  Max - Min: {}".format(int(maxValue - minValue)))
