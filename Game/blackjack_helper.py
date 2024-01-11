from random import randint

# Prints the given card's official name in the form "Drew a(n) ___".
# If the input card is invalid, prints "BAD CARD"
# 
# Parameters:
#   card_rank: The numeric representation of a card (1-13)
#
# Return:
#   none
def print_card_name(card_rank):
    # Implement card_name function here
    if card_rank < 1 or card_rank > 13:
        print("BAD CARD")
    else:
        if card_rank == 1:
            card_name = "Ace"
        elif card_rank == 11:
            card_name = "Jack"
        elif card_rank == 12:
            card_name = "Queen"
        elif card_rank == 13:
            card_name = "King"
        else:
            card_name = str(card_rank)
            
        if card_rank == 1 or card_rank == 8:
            print("Drew an " + card_name)
        else:
            print("Drew a " + card_name)
    
# Draws a new random card, prints its name, and returns its value.
# 
# Parameters:
#   none
#
# Return:
#   an int representing the value of the card. All cards are worth
#   the same as the card_rank except Jack, Queen, King, and Ace.
def draw_card():
    draw_card = randint(1, 13)
    if draw_card == 11 or draw_card == 12 or draw_card == 13:
        print_card_name(draw_card)
        return 10
    if draw_card == 1:
        print_card_name(draw_card)
        return 11
    print_card_name(draw_card)
    return draw_card


# Prints the given message formatted as a header. A header looks like:
# -----------
# message
# -----------
# 
# Parameters:
#   message: the string to print in the header
#
# Return:
#   none
def print_header(message):

    # Implement print_header function here
    print("-----------\n{}\n-----------".format(message))
# Prints turn header and draws a starting hand, which is two cards.
# 
# Parameters:
#   name: The name of the player whose turn it is.
#
# Return:
#   The hand total, which is the sum of the two newly drawn cards.
def draw_starting_hand(name):
    # Implement draw_starting_hand function here
    print_header(name + " TURN")
    card1 = draw_card()
    card2 = draw_card()
    return card1 + card2
# Prints the hand total and status at the end of a player's turn.
#
# Parameters:
#   hand_value: the sum of all of a player's cards at the end of their turn.
# Return:
#   none
def print_end_turn_status(hand_value):
    # Implement print_end_turn_status function here
    print("Final hand: {}.".format(hand_value))
    if hand_value == 21:
        print("BLACKJACK!")
    elif hand_value > 21:
        print("BUST.") 
# Prints the end game banner and the winner based on the final hands.
# 
# Parameters:
#   user_hand: the sum of all cards in the user's hand
#   dealer_hand: the sum of all cards in the dealer's hand
#
# Return:
#   none
def print_end_game_status(user_hand, dealer_hand):
    # Implement print_end_game_status function here
    print_header("GAME RESULT")
    if user_hand <= 21 and user_hand == dealer_hand:
        print("Push.")
    elif user_hand < 21 and user_hand < dealer_hand and dealer_hand <= 21 or user_hand > 21:
        print("Dealer wins!")
    elif user_hand <= 21:
        if user_hand > dealer_hand or dealer_hand > 21:
            print("You win!")
