deck = []

hand = []
hand.append([])
hand.append([])

text = ""

for i in range(0, 52):
    deck.append(i+1)
    deck[i] = deck[i] % 13

    if deck[i] == 0:
        deck[i] = "Ace"

    elif deck[i] == 11:
        deck[i] = "Jack"

    elif deck[i] == 12:
        deck[i] = "Queen"

    elif deck[i] == 0:
        deck[i] = "King"

    print deck[i]

