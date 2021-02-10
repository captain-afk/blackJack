import random

suits = [" of Hearts", " of Diamonds", " of Clubs", " of Spades"]
cardValues = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
tenPointCards = ["10", "J", "Q", "K"]


def makeDeck():
    deck = []
    for suit in suits:
        for card in cardValues:
            deck.append(card+suit)
    return(deck)

def shuffleDeck():
    deck = makeDeck()
    random.shuffle(deck)
    return(deck)

def dealCards(deck):
    playerHand = []
    dealerHand = []

    playerHand.append(deck.pop(0))
    playerHand.append(deck.pop(0))

    dealerHand.append(deck.pop(0))
    dealerHand.append(deck.pop(0))

    return(playerHand, dealerHand, deck)

def hitMe(hand, deck):
    hand.append(deck.pop(0))
    return(hand, deck)

def checkPointsInHand(hand):
    pointValue = 0
    aceCount = 0
    for card in hand:
        cardValue = card.split(" ")[0]
        if cardValue in tenPointCards:
            pointValue += 10
        elif cardValue == "A":
            aceCount += 1
            pointValue += 11
        else:
            pointValue += int(cardValue)
    for x in range(aceCount):
        if pointValue > 21:
            pointValue -= 10
    return(pointValue)


def checkWinner(dealerPoints, playerPoints):
    if dealerPoints >= playerPoints:
        winner = "dealer"
    else:
        winner = "player"
    return(winner)

def main():
    print("Welcome to the Black Jack table.")
    deck = shuffleDeck()
    playerHand, dealerHand, deck = dealCards(deck)
    dealerPoints = checkPointsInHand(dealerHand)
    while True:
        playerPoints = checkPointsInHand(playerHand)
        print("You are showing:", playerHand,f"({playerPoints})")
        print("Dealer is showing:", dealerHand,f"({dealerPoints})")
        if playerPoints == 21:
            print("Blackjack baby! You win!")
            break
        if dealerPoints == 21:
            print("Blackjack for the dealer. Dealer wins.")
            break
        if playerPoints > 21:
            print("Bummer, you busted. Dealer wins")
            break
        print("Do you want to hit or stand?")
        playerChoice = input().lower()
        if playerChoice == 'hit':
            playerHand, deck = hitMe(playerHand,deck)
            print('hit it chewie')
        elif playerChoice == 'stand':
            print('red leader standing by')
            while dealerPoints < 17:
                print("Dealer hits!")
                dealerHand, deck = hitMe(dealerHand,deck)
                dealerPoints = checkPointsInHand(dealerHand)
                print("Dealer is showing:", dealerHand,f"({dealerPoints})")
            if dealerPoints > 21:
                print("Dealer busted! You Win!")
                break
            else:
                winner = checkWinner(dealerPoints,playerPoints)
                print("aaaaaand the winner is the", winner)
                break

main()