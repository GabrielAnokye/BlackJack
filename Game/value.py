card_rank = int(input())

if card_rank == 11 or card_rank == 12 or card_rank == 13:
  # Jacks, Queens, and Kings are worth 10.
  card_value = 10
elif card_rank == 1:
  # Aces are worth 11.
  card_value = 11
else:
  # All other cards are worth the same as
  # their rank.
  card_value = card_rank

if card_rank > 13 or card_rank < 1:
  print('BAD CARD')
else:
  print('Your hand value is ' + str(card_value) + '.')
