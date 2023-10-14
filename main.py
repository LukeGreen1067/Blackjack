#TODO: Add a loop to the gameplay and add the feature of money in
#TODO: Add insurance and splitting
#TODO: Add deck checking for multiple cards and discarded cards e.g. 2x Ace of Diamonds (Basically add card counting)

#TODO: Maybe add functionality to pick the amount of decks you want

# https://en.wikipedia.org/wiki/Blackjack

import random

suit = ["Diamonds", "Hearts", "Clubs", "Spades"]
number = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, "Jack", "Queen", "King"]

nameNumbers = ["Jack", "Queen", "King"]

dealersCards = []
gamblersCards = []

testHand = [['Ace', 'Hearts'], [8, 'Clubs'], [5, 'Spades']]
testHand2 = [['Ace', 'Hearts'], ['King', 'Clubs']]

money = 500


# gets a random card from the deck (Doesnt check for duplicates)
def getCard():
    Value = number[random.randint(0, len(number) - 1)]
    Suit = suit[random.randint(0, len(suit) - 1)]
    return [Value, Suit]


# gets the value of any given hand
def getHandValue(hands):
    value = 0
    for hand in hands:
        if any([x in hand for x in nameNumbers]):
            value += 10
        elif "Ace" in hand:
            if value + 11 > 21:
                value += 1
            else:
                value += 11
        else:
            value += hand[0]

    for hand in hands:
        if "Ace" in hand and value > 21:
            value -= 10  # Cant find a better way to not bust on the Aces when 1 and 11 are available

    return value


def initialDeal():
    dealersCards.append(getCard())
    dealersCards.append(getCard())
    gamblersCards.append(getCard())
    gamblersCards.append(getCard())


def showHand(hand):  # Shows the hand of the player hate the code tho need to get rid of temp
    temp = ""
    for i in hand:
        temp += f"{i[0]} of {i[1]} and the "
    return temp

def dealersTurn(gamblersCards, dealersCards):
    while getHandValue(gamblersCards) > getHandValue(dealersCards):

        if getHandValue(dealersCards) == 21:
            return 1
        elif getHandValue(dealersCards) >= 17:
            return 2
        else:
            gamblersCards.append(getCard())
    return False


flag = True

while flag:
    initialDeal()

    bet = input(f"How much would you like to bet you have £{money} remaining: ")
    print(f"Your cards are {showHand(gamblersCards)}giving you a value of {getHandValue(gamblersCards)}")

    choice = input("Would you like to hit or stand")
    if choice == "Hit":
        gamblersCards.append(getCard())
    elif choice == "Stand":
        # Do something
        print('hi')
    else:
        print("I dont understand your input try again")

    flag = False
