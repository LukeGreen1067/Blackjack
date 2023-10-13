# class Card:
#     Number = 0
#     Suit = ""
#
#     def __init__(self, N, S):
#         self.Number = N
#         self.Suit = S
#
#     def getCard(self):
#

import random

suit = ["Diamonds", "Hearts", "Clubs", "Spades"]
number = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, "Jack", "Queen", "King"]

nameNumbers = ["Ace", "Jack", "Queen", "King"]

dealersCards = []
gamblersCards = []

testHand = [['Ace', 'Hearts'], [8, 'Clubs'], [5, 'Spades']]

# gets a random card from the deck (Doesnt check for duplicates)
def getCard():
    Value = number[random.randint(0, len(number) - 1)]
    Suit = suit[random.randint(0, len(suit) - 1)]
    return [Value, Suit]

#gets the value of any given hand
def getHandValue(hands):
    value = 0
    for hand in hands:
        if any([x in hand for x in nameNumbers]):
            value += 10
        elif "Ace" in hand:
            if value + 11 < 21:
                value += 1
            else:
                value += 11
        else:
            value += hand[0]

    for hand in hands:
        if "Ace" in hand and value > 21:
            value -= 10

    return value

while True:
    dealersCards.append(getCard())
    dealersCards.append(getCard())
    gamblersCards.append(getCard())
    gamblersCards.append(getCard())

    print(f"Your cards are {gamblersCards[0][0]} of {gamblersCards[0][1]} and the {gamblersCards[1][0]} of {gamblersCards[1][1]} "
          f"giving a value of {getHandValue(gamblersCards)}")




    break