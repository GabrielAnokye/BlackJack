# DO NOT CHANGE OR REMOVE THIS COMMENT, and do not change this import otherwise all tests will fail.
# Use randint to generate random cards. 
from random import randint

# Write all of your part 2B code below this comment. DO NOT CHANGE OR REMOVE THIS COMMENT.

# Draw 1st card.
card1_rank = randint(1, 13)
if card1_rank == 1:
  # A 1 stands for an ace.
  card1_name = "Ace"
elif card1_rank == 11:
  # An 11 stands for a jack.
  card1_name = "Jack"
elif card1_rank == 12:
  # A 12 stands for a queen.
  card1_name = "Queen"
elif card1_rank == 13:
  # A 13 stands for a king.
  card1_name = "King"
else:
  # All other cards are named by their number, or rank.
  card1_name = str(card1_rank)

if card1_rank == 1 or card1_rank == 8:
  print('Drew an ' + card1_name)
else:
  print('Drew a ' + card1_name)

if card1_rank == 11 or card1_rank == 12 or card1_rank == 13:
  # Jacks, Queens, and Kings are worth 10.
  card1_value = 10
elif card1_rank == 1:
  # Aces are worth 11.
  card1_value = 11
else:
  # All other cards are worth the same as their rank.
  card1_value = card1_rank

# Draw 2nd card.
card2_rank = randint(1, 13)
if card2_rank == 1:
  # A 1 stands for an ace.
  card2_name = "Ace"
elif card2_rank == 11:
  # An 11 stands for a jack.
  card2_name = "Jack"
elif card2_rank == 12:
  # A 12 stands for a queen.
  card2_name = "Queen"
elif card2_rank == 13:
  # A 13 stands for a king.
  card2_name = "King"
else:
  # All other cards are named by their
  # number, or rank.
  card2_name = str(card2_rank)

if card2_rank == 1 or card2_rank == 8:
  print('Drew an ' + card2_name)
else:
  print('Drew a ' + card2_name)

if card2_rank == 11 or card2_rank == 12 or card2_rank == 13:
  # Jacks, Queens, and Kings are worth 10.
  card2_value = 10
elif card2_rank == 1:
  # Aces are worth 11.
  card2_value = 11
else:
  # All other cards are worth the same as their rank.
  card2_value = card2_rank

hand_value = card1_value + card2_value

# The user has the option to keep drawing if their hand is below 21.
while hand_value < 21:
  should_hit = input('You have ' + str(hand_value) + ". Hit (y/n)? ")
  if should_hit == 'n':
    break
  elif should_hit == 'y':
    card_rank = randint(1, 13)
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
        # All other cards are named by their
        # number, or rank.
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

    hand_value = hand_value + card_value
  else:
    print("Sorry I didn't get that.")

print("Final hand: " + str(hand_value) + ".")
if hand_value == 21:
    print("BLACKJACK!")
elif hand_value > 21:
    print("BUST.")
