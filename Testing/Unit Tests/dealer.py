# DO NOT CHANGE OR REMOVE THIS COMMENT, and do not change this import otherwise all tests will fail.
# Use randint to generate random cards. 
from random import randint

# Write all of your part 2A code below this comment. DO NOT CHANGE OR REMOVE THIS COMMENT.
hand_value = 0
num_cards = 0
while hand_value < 17:
  card_rank = randint(1, 13)
  num_cards += 1
  if card_rank == 1:
    # A 1 stands for an ace.
    card_name = "Ace"
  elif card_rank == 11:
    # An 11 stands for a jack.
    card_name = "Jack"
  elif card_rank == 12:
    # A 12 stands for a queen.
    card_name = "Queen"
  elif card_rank == 13:
    # A 13 stands for a king.
    card_name = "King"
  else:
    # All other cards are named by their number, or rank.
    card_name = str(card_rank)

  if card_rank == 1 or card_rank == 8:
    print('Drew an ' + card_name)
  else:
    print('Drew a ' + card_name)

  if card_rank == 11 or card_rank == 12 or card_rank == 13:
    # Jacks, Queens, and Kings are worth 10.
    card_value = 10
  elif card_rank == 1:
    # Aces are worth 11.
    card_value = 11
  else:
    # All other cards are worth the same as their rank.
    card_value = card_rank

  hand_value += card_value
  if num_cards > 1 and hand_value < 17:
    print("Dealer has {}.".format(hand_value))
  
print("Final hand: " + str(hand_value) + ".")
if hand_value == 21:
    print("BLACKJACK!")
elif hand_value > 21:
    print("BUST.")
