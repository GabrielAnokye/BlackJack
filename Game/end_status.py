hand = int(input())

if hand == 21:
  print('BLACKJACK!')
elif hand > 21 and hand <= 31:
  print('BUST.')
elif hand > 31 or hand < 4:
  print('BAD HAND VALUE!')
