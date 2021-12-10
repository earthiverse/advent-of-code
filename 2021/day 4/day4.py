# Prepare numbers & cards
numbers = []
cards = []
with open('day4_input.csv') as file:
    numbers = list(map(int, file.readline().split(",")))

    while True:
        try:
            next(file)
            card = [list(map(int, next(file).split())) for x in range(5)]
            card = [item for sublist in card for item in sublist]
            cards.append(card)
        except StopIteration:
            break

for number in numbers:
    # Mark the new card
    for card in cards:
        for i in range(25):
            if card[i] == number:
                card[i] = "X"
    
    toDelete = []
    for k in range(len(cards)):
        card = cards[k]

        completed = -1
        # Row Checks
        for i in range(0, 25, 5):
            bingo = True
            for j in range(i, i + 5):
                if card[j] != "X":
                    bingo = False
                    break
            if bingo:
                completed = k
                break
        
        # Column Checks
        if not bingo:
            for i in range(0, 5):
                bingo = True
                for j in range(i, 25, 5):
                    if card[j] != "X":
                        bingo = False
                        break
                if bingo:
                    completed = k
                    break

        # Diagonal 1 Check (forward)
        # if not bingo:
        #     for i in range(0, 25, 6):
        #         bingo = True
        #         if card[i] != "X":
        #             bingo = False
        #             break
        
        # Diagonal 2 Check (backward)
        # if not bingo:
        #     for i in range(4, 25, 4):
        #         bingo = True
        #         if card[i] != "X":
        #             bingo = False
        #             break
        
        if bingo == True:
            toDelete.append(completed)

    toDelete.sort(reverse=True)
    for completed in toDelete:
        total = 0
        for i in cards[completed]:
            if i != "X":
                total += i

        print("BINGO! {}, {}, {}".format(total, number, total * number))
        del cards[completed]