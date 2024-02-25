##  Day 11 - Section 10:- Beginner - The Blackjack Capstone Project

''' Blackjack game:

You are tasked with implementing a simplified version of Blackjack in Python. The rules are as follows:

Players are dealt two cards each initially.
The goal is to have a hand value as close to 21 as possible without exceeding it.
Cards 2 through 10 are worth their face value, while Jacks, Queens, and Kings are worth 10 points each.
Aces can count as either 1 or 11, depending on which value is more advantageous.
If a player's hand value exceeds 21, they bust and lose the game.
If both the player and the dealer have the same hand value, it's a draw.
The dealer must hit (draw another card) if their hand value is 16 or lower.
The game uses an infinite deck, meaning cards are not removed after being drawn.
Your task is to write a Python function play_blackjack() that simulates a single game of Blackjack between a player and a dealer. The function should take no arguments and should return one of the following strings based on the outcome of the game: "Player wins", "Dealer wins", or "Draw".

You can assume that input validation is not required for this task.

Our Blackjack game rules
## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
'''


import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
                   

                                      
     
print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_cards(cards_computer):
    """Deals a card from the deck."""
    cards_computer.append(random.choice(cards))

def calculate_sum(hand):
    """Calculates the sum of the hand."""
    # If sum exceeds 21 and there's an ace, count ace as 1 instead of 11
    if sum(hand) > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
    return sum(hand)

def play_blackjack():
    """Simulates a single game of Blackjack."""
    cards_player = []
    cards_computer = []
    
    # Deal initial cards
    deal_cards(cards_computer)
    deal_cards(cards_player)
    deal_cards(cards_computer)
    deal_cards(cards_player)
    
    player_score = calculate_sum(cards_player)
    computer_score = calculate_sum(cards_computer)
    
    print(f"Your cards: {cards_player}, current score: {player_score}")
    print(f"Computer's first card: {cards_computer[0]}")
    
    while player_score < 21:
        another_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if another_card == 'y':
            deal_cards(cards_player)
            player_score = calculate_sum(cards_player)
            print(f"Your cards: {cards_player}, current score: {player_score}")
            print(f"Computer's first card: {cards_computer[0]}")
        else:
            break
    
    while computer_score < 17:
        deal_cards(cards_computer)
        computer_score = calculate_sum(cards_computer)
    
    print_final_hand(cards_player, cards_computer, player_score, computer_score)

def print_final_hand(cards_player, cards_computer, player_score, computer_score):
    """Prints the final hands and scores."""
    print(f"Your final hand: {cards_player}, final score: {player_score}")
    print(f"Computer's final hand: {cards_computer}, final score: {computer_score}")
    
    if player_score > 21:
        print("Your score exceeded 21, you lose. Computer wins.")
    elif computer_score > 21:
        print("Computer's score exceeded 21, you win.")
    elif player_score == computer_score:
        print("It's a draw.")
    elif player_score > computer_score:
        print("You win. Computer loses.")
    else:
        print("Computer wins. You lose.")

play_blackjack()
