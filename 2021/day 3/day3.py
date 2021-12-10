data = []
with open('day3_input.csv') as file:
    data = file.read().splitlines()

counts = []
for i in data[0]:
    counts.append([0, 0])

for datum in data:
    for i in range(0, len(datum)):
        digit = int(datum[i])
        counts[i][digit] += 1

leastCommon = ""
mostCommon = ""
for count in counts:
    if(count[0] > count[1]):
        mostCommon += "0"
        leastCommon += "1"
    else:
        mostCommon += "1"
        leastCommon += "0"

gamma = int(mostCommon, 2)
sigma = int(leastCommon, 2)
print("gamma => {}: {}".format(mostCommon, gamma))
print("sigma => {}: {}".format(leastCommon, sigma))
print("power => {}".format(sigma * gamma))

numDigits = len(data[0])
examine = data.copy()
examineCounts = counts[0]
confirmed = []
confirmedCounts = [0, 0]
for i in range(0, numDigits):
    keep = "1"
    if(examineCounts[0] > examineCounts[1]):
        keep = "0"

    for e in examine:
        #print("checking {} vs {}".format(e[i], keep))
        if(e[i] == keep):
            confirmed.append(e)
            if(i < numDigits - 1):
                confirmedCounts[int(e[i+1])] += 1

    if(len(confirmed) == 1):
        o2 = int(confirmed[0], 2)
        print("oxygen => {}: {}".format(confirmed[0], o2))

    examine = confirmed
    examineCounts = confirmedCounts
    confirmed = []
    confirmedCounts = [0, 0]

examine = data.copy()
examineCounts = counts[0]
confirmed = []
confirmedCounts = [0, 0]
for i in range(0, numDigits):
    keep = "0"
    if(examineCounts[0] > examineCounts[1]):
        keep = "1"

    for e in examine:
        if(e[i] == keep):
            confirmed.append(e)
            if(i < numDigits - 1):
                confirmedCounts[int(e[i+1])] += 1

    if(len(confirmed) == 1):
        co2 = int(confirmed[0], 2)
        print("co2 => {}: {}".format(confirmed[0], co2))
        break

    examine = confirmed
    examineCounts = confirmedCounts
    confirmed = []
    confirmedCounts = [0, 0]

print("life support => {}".format(co2 * o2))