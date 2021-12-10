data = []
with open('day5_input.txt') as file:
    data = file.read().splitlines()

seats = []
for datum in data:
    # Row
    min_row = 0
    max_row = 2 ** 7 - 1
    for c in range(0,7):
        diff = max_row + 1 - min_row
        if datum[c] == "F":
            max_row = max_row - (diff // 2)
        else: # datum[c] == "B"
            min_row = min_row + (diff // 2)

    # Column
    min_col = 0
    max_col = 2 ** 3 - 1
    for c in range(7, 10):
        diff = max_col + 1 - min_col
        if(datum[c] == "L"):
           max_col = max_col - (diff // 2)
        else: #datum[c] == "R"
            min_col = min_col + (diff // 2)

    seat = min_row * 8 + min_col
    seats.append(seat)

seats.sort()
print(f"maximum seat number: {seats[len(seats) - 1]}")

for i in range(0, len(seats) - 1):
    if seats[i + 1] != seats[i] + 1:
        print(f"our seat number: {i + seats[0] + 1}")
