card_rank = int(input())

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
  drew_prefix = 'Drew an '
else:
  drew_prefix = 'Drew a '

if card_rank < 1 or card_rank > 13:
  print('BAD CARD')
else:
  print(drew_prefix + card_name)
