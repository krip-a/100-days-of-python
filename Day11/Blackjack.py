# imports
import random
from Blackjack_Art import logo

# a function to get a card:
def get_card():
    """return a random card fromt the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    chosen_card = random.choice(cards)
    return chosen_card

def calculate_score(cards):
    """take a list of cards and return the score"""
    # if 11 in cards and 10 in cards and len(cards) == 2:
    if sum(cards) == 21 and len(cards) == 2:    #BlackJack
        return 0
    while 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def get_card_value(this_hand):
    new_card = get_card()
    
    if new_card == 11:
        new_hand = this_hand.copy()
        new_hand.append(new_card)
        current_score = sum(new_hand)

        if current_score > 21:
            return 1
        else:
            return 11
    else:
        return new_card

def check_score(player_cards, computer_cards):
    player_score = calculate_score(player_cards)
    computer_score = calculate_score(computer_cards)

    if player_score == computer_score:
        print("Draw")
    elif computer_score == 0:
        print("Computer's BlackJack. You lose :(")
    elif player_score == 0:
        print("BlackJack! You win")
    elif player_score > 21:
        print("Bust! You went over 21. You lost :( ")
    elif computer_score > 21:
        print("Computer bust. You win!")
    elif player_score > computer_score:
        print("You were closer to 21 than Computer. You win!")   
    else:
        print("Computer was closer to 21 than you. You lost :( ")
        
run_game = True
while run_game:
    want_to_play = input("Do you want to play a game of Blackjack? 'y' or 'n': ").lower()
    if want_to_play == "y": 
        run_game = True
        print(logo)
    else:
        run_game = False
        continue

    player_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):                                  # dealing 2 cards each 
        player_cards.append(get_card())
        computer_cards.append(get_card())   
    
    player_score = calculate_score(player_cards)
    computer_score = calculate_score(computer_cards)

    print(f"Your cards: {player_cards}, your current score: {player_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    if player_score == 0 or computer_score == 0 or player_score > 21:
        is_game_over = True
    
    while not is_game_over:                 # hit, take another card
        add_card = input("Type 'y' to get new card and 'n' to pass: ").lower()
        if add_card == "y":
            player_cards.append(get_card_value(player_cards))
            player_score = calculate_score(player_cards)

            if player_score >= 21:
                is_game_over = True
        else:
            is_game_over = True
    
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(get_card_value(computer_cards))   # get another card
        computer_score = calculate_score(computer_cards)
    
    print(f"\nYour final hand: {player_cards}, your final score: {player_score}")
    print(f"Computer's final hand: {computer_cards}, Computer's final score: {computer_score}")
    print("**********"*10)
    check_score(player_cards, computer_cards)
    print("Game Over.")
    print("**********"*10)
    print("\n"*3)
    

  
