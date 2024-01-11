from blackjack_helper import *

user_hand = draw_starting_hand("YOUR")
while user_hand < 21:
  should_hit = input("You have {}. Hit (y/n)? ".format(user_hand))
  if should_hit.lower() == "n":
    break
  elif should_hit.lower() == "y":
    new_hand = draw_card()
    user_hand += new_hand
  else:
    print("Sorry I didn't get that.")
print_end_turn_status(user_hand)

dealer_hand = draw_starting_hand("DEALER")
while dealer_hand < 17:
  print("Dealer has {}.".format(dealer_hand))
  new_hand1 = draw_card()
  dealer_hand += new_hand1
print_end_turn_status(dealer_hand)

print_end_game_status(user_hand, dealer_hand)
