# TODO: Add a loop to the gameplay and add the feature of money in
# TODO: Add insurance and splitting
# TODO: Add deck checking for multiple cards and discarded cards e.g. 2x Ace of Diamonds (Basically add card counting)


# TODO: Maybe add functionality to pick the amount of decks you want

# https://en.wikipedia.org/wiki/Blackjack

# The Dealer's Play When the dealer has served every player, the dealers face-down card is turned up. If the total is
# 17 or more, it must stand. If the total is 16 or under, they must take a card. The dealer must continue to take
# cards until the total is 17 or more, at which point the dealer must stand. If the dealer has an ace, and counting
# it as 11 would bring the total to 17 or more (but not over 21), the dealer must count the ace as 11 and stand. The
# dealer's decisions, then, are automatic on all plays, whereas the player always has the option of taking one or
# more cards.

# That was acutally crazy hard to find took me like 20 mins of googling to find the dealers rules????

import random

suit = ["Diamonds", "Hearts", "Clubs", "Spades"]
number = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, "Jack", "Queen", "King"]

nameNumbers = ["Jack", "Queen", "King"]

dealersCards = []
gamblersCards = []

testHand = [['Ace', 'Hearts'], [8, 'Clubs'], [5, 'Spades']]
testHand2 = [['Ace', 'Hearts'], [8, 'Clubs']]
testHand3 = [['Ace', 'Hearts'], [8, 'Clubs'], [2, 'Spades'], [5, 'Spades']]

money = 500


# gets a random card from the deck (Doesn't check for duplicates)
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
        if i == hand[-1:][0]:
            temp += f"{i[0]} of {i[1]} "
        else:
            temp += f"{i[0]} of {i[1]} and the "
    return temp


def dealersTurn(Cards):
    # If the total is 17 or more, it must stand
    if getHandValue(Cards) >= 17:
        print(f"The dealer has chosen to stand with the hand {showHand(Cards)}")
        return "Stand"
    # If the total is 16 or under, they must take a card.
    elif getHandValue(Cards) <= 16:
        print(f"The dealer has hit the hand is now {showHand(Cards)}")
        Cards.append(getCard())
        dealersTurn(Cards)
        if getHandValue(Cards) > 21:
            return "Bust"
        else:
            return "Stand"
    # If the dealer has an ace, and counting it as 11 would bring the total to 17 or more (but not over 21), the dealer
    # must count the ace as 11 and stand.
    # This is already satisfied by the getHandValue thankfully


def determineWinner(playerCards, dealerCards):
    playerValue = getHandValue(playerCards)
    dealerValue = getHandValue(dealerCards)
    if playerValue > dealerValue:
        return f"The player wins the hand with a value of {getHandValue(playerCards)}"
    elif playerValue < dealerValue:
        return f"The dealer wins the hand with a value of {getHandValue(dealerCards)}"
    else:
        return "Standoff money is returned"


flag = True
game = True

while flag:
    initialDeal()

    bet = input(f"How much would you like to bet you have £{money} remaining: ")
    print(f"Your cards are {showHand(gamblersCards)}giving you a value of {getHandValue(gamblersCards)}")
    print(f"The dealer has the revealed {dealersCards[0][0]} of {dealersCards[0][1]}")

    # TODO: After 15/10/23 adding functionality and finding the dealers play need to fix game funtionality however too
    #  tired tonight gonna eat then sleep. Hint for tommorow: Its the stupid showHand function that you hate
    while game:
        choice = input("Would you like to hit or stand ")
        if choice == "Hit":
            gamblersCards.append(getCard())
            if getHandValue(gamblersCards) > 21:
                print("You have gone bust")
                break
            else:
                print(f"Your hand is now {showHand(gamblersCards)}giving you a value of {getHandValue(gamblersCards)}")
        elif choice == "Stand":
            print(f"The dealers hand is {showHand(dealersCards)}")
            dealerOutcome = dealersTurn(dealersCards)
            if dealerOutcome == "Stand":
                print(determineWinner(gamblersCards, dealersCards))
                break
            elif dealerOutcome == "Bust":
                print("The dealer has gone bust you win")
                break
        else:
            print("I dont understand your input try again")

    play = input("Would you like to play again? Y/N ")


    if play.upper() == "Y":
        dealersCards.clear()
        gamblersCards.clear()
        continue
    elif play.upper() == "N":
        flag = False
    else:
        dealersCards.clear()
        gamblersCards.clear()
        continue
