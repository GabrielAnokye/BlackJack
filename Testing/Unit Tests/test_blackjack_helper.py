from blackjack_helper import *
from test_helper import *
import unittest

class TestBlackjackHelper(unittest.TestCase):
  """
  Class for testing blackjack helper functions.
  """

  def test_print_card_name_example(self):
    """
    Example of a test to compare printed statements with expected

    """
    self.assertEqual(get_print(print_card_name, 2), "Drew a 2\n")

  def test_mock_randint_example(self):
    """
    Example of a test to compare output for a function that calls randint

    """
    self.assertEqual(mock_random([3], draw_card), 3)
    self.assertEqual(mock_random([3, 5], draw_starting_hand, "DEALER"), 8)

  # MAKE SURE ALL YOUR FUNCTION NAMES BEGIN WITH test_

  def test_print_card_name(self):
    self.assertEqual(get_print(print_card_name, 1), "Drew an Ace\n")
    self.assertEqual(get_print(print_card_name, 11), "Drew a Jack\n")
    self.assertEqual(get_print(print_card_name, 12), "Drew a Queen\n")
    self.assertEqual(get_print(print_card_name, 13), "Drew a King\n")
    self.assertEqual(get_print(print_card_name, 8), "Drew an 8\n")
    self.assertEqual(get_print(print_card_name, 4), "Drew a 4\n")

  def test_draw_card(self):
    self.assertEqual(mock_random([1], draw_card), 11)
    self.assertEqual(mock_random([11], draw_card), 10)
    self.assertEqual(mock_random([12], draw_card), 10)
    self.assertEqual(mock_random([13], draw_card), 10)
    self.assertEqual(mock_random([2], draw_card), 2)
    self.assertEqual(mock_random([8], draw_card), 8)

  def test_print_header(self):
    self.assertEqual(get_print(print_header, "DEALER"), "-----------\nDEALER\n-----------\n")
    self.assertEqual(get_print(print_header, "YOUR"), "-----------\nYOUR\n-----------\n")
    self.assertEqual(get_print(print_header, "GAME RESULT"), "-----------\nGAME RESULT\n-----------\n")

  def test_draw_starting_hand(self):
    self.assertEqual(mock_random([1, 7], draw_starting_hand, "DEALER"), 18)
    self.assertEqual(mock_random([1, 11], draw_starting_hand, "DEALER"), 21)
    self.assertEqual(mock_random([1, 12], draw_starting_hand, "DEALER"), 21)
    self.assertEqual(mock_random([13, 1], draw_starting_hand, "YOUR"), 21)
    self.assertEqual(mock_random([12, 3], draw_starting_hand, "YOUR"), 13)
    self.assertEqual(mock_random([11, 9], draw_starting_hand, "YOUR"), 19)
    self.assertEqual(mock_random([4, 7], draw_starting_hand, "YOUR"), 11)
    self.assertEqual(mock_random([8, 6], draw_starting_hand, "DEALER"), 14)
    
  def test_print_end_turn_status(self):
    self.assertEqual(get_print(print_end_turn_status, 21), "Final hand: 21.\nBLACKJACK!\n")
    self.assertEqual(get_print(print_end_turn_status, 24), "Final hand: 24.\nBUST.\n")
    self.assertEqual(get_print(print_end_turn_status, 18), "Final hand: 18.\n")
    self.assertEqual(get_print(print_end_turn_status, 7), "Final hand: 7.\n")

  def test_print_end_game_status(self):
    self.assertEqual(get_print(print_end_game_status, 21, 20), "-----------\nGAME RESULT\n-----------\nYou win!\n")
    self.assertEqual(get_print(print_end_game_status, 20, 18), "-----------\nGAME RESULT\n-----------\nYou win!\n")
    self.assertEqual(get_print(print_end_game_status, 17, 24), "-----------\nGAME RESULT\n-----------\nYou win!\n")
    self.assertEqual(get_print(print_end_game_status, 21, 22), "-----------\nGAME RESULT\n-----------\nYou win!\n")
    self.assertEqual(get_print(print_end_game_status, 23, 23), "-----------\nGAME RESULT\n-----------\nDealer wins!\n")
    self.assertEqual(get_print(print_end_game_status, 20, 21), "-----------\nGAME RESULT\n-----------\nDealer wins!\n")
    self.assertEqual(get_print(print_end_game_status, 24, 19), "-----------\nGAME RESULT\n-----------\nDealer wins!\n")
    self.assertEqual(get_print(print_end_game_status, 17, 19), "-----------\nGAME RESULT\n-----------\nDealer wins!\n")
    self.assertEqual(get_print(print_end_game_status, 21, 21), "-----------\nGAME RESULT\n-----------\nPush.\n")
    self.assertEqual(get_print(print_end_game_status, 19, 19), "-----------\nGAME RESULT\n-----------\nPush.\n")


if __name__ == '__main__':
    unittest.main()
