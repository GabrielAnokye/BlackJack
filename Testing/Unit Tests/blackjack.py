# Use randint to generate random cards. 
from blackjack_helper import *


# USER'S TURN
user_hand = draw_starting_hand("YOUR")
should_hit = 'y'
while user_hand < 21:
  should_hit = input("You have {}. Hit (y/n)? ".format(user_hand))
  if should_hit == 'n':
    break
  elif should_hit != 'y':
    print("Sorry I didn't get that.")
  else:
    user_hand = user_hand + draw_card()
print_end_turn_status(user_hand)
  
# DEALER'S TURN
dealer_hand = draw_starting_hand("DEALER")
while dealer_hand < 17:
  print("Dealer has {}.".format(dealer_hand))
  dealer_hand = dealer_hand + draw_card()
print_end_turn_status(dealer_hand)

# GAME RESULT
print_end_game_status(user_hand, dealer_hand)
