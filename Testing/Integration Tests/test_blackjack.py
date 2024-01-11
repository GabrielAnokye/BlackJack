from unittest import TestCase, main
from unittest.mock import patch
from test_helper import run_test

class TestBlackjack(TestCase):

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_example(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand less than 21.
        The dealer wins by having a higher hand than the user.

        '''
        output = run_test([3, 5, 8], ['y', 'n'], [3, 5, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "You have 8. Hit (y/n)? y\n" \
                   "Drew an 8\n" \
                   "You have 16. Hit (y/n)? n\n" \
                   "Final hand: 16.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "Dealer has 8.\n" \
                   "Drew a 10\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)

    # Make sure all your test functions start with test_ 
    # ALL YOUR TESTS BELOW.
    
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_win_blackjack(self, input_mock, randint_mock):
        '''
        The user receives cards the combines to give 21 but the dealer did not.
        The user wins for hitting a Blackjack and dealer having total cards sum less than 21.
        '''
        output = run_test([12, 1,], [], [2, 7, 13], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a Queen\n" \
                   "Drew an Ace\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 2\n" \
                   "Drew a 7\n" \
                   "Dealer has 9.\n" \
                   "Drew a King\n" \
                   "Final hand: 19.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_win_greater_value(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand less than 21.
        The user wins by having a higher hand than the dealer.
        '''
        output = run_test([13, 8, 2], ['y', 'n'], [8, 11], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a King\n" \
                   "Drew an 8\n" \
                   "You have 18. Hit (y/n)? y\n" \
                   "Drew a 2\n" \
                   "You have 20. Hit (y/n)? n\n" \
                   "Final hand: 20.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew an 8\n" \
                   "Drew a Jack\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_win_dealer_Bust(self, input_mock, randint_mock):
        '''
        The user receives cards that end up with a hand less than 21 and dealer hand more than 21
        The user wins since dealer Bust.
        '''
        output = run_test([5, 5, 7], ['y', 'n'], [11, 6, 8], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 5\n" \
                   "Drew a 5\n" \
                   "You have 10. Hit (y/n)? y\n" \
                   "Drew a 7\n" \
                   "You have 17. Hit (y/n)? n\n" \
                   "Final hand: 17.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a Jack\n" \
                   "Drew a 6\n" \
                   "Dealer has 16.\n" \
                   "Drew an 8\n" \
                   "Final hand: 24.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_win_dealer_bust(self, input_mock, randint_mock):
        '''
        The user receives cards that end up with a hand of 21 and dealer hand more than 21.
        The user wins by having a Blackjack and dealer bust.
        '''
        output = run_test([6, 8, 7], ['y', 'n'], [8, 5, 9], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 6\n" \
                   "Drew an 8\n" \
                   "You have 14. Hit (y/n)? y\n" \
                   "Drew a 7\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew an 8\n" \
                   "Drew a 5\n" \
                   "Dealer has 13.\n" \
                   "Drew a 9\n" \
                   "Final hand: 22.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer_win_user_bust_same_values(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand greater than 21.
        The dealer wins since user Bust.
        '''
        output = run_test([5, 5, 8, 5], ['y', 'y'], [8, 5, 12], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 5\n" \
                   "Drew a 5\n" \
                   "You have 10. Hit (y/n)? y\n" \
                   "Drew an 8\n" \
                   "You have 18. Hit (y/n)? y\n" \
                   "Drew a 5\n" \
                   "Final hand: 23.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew an 8\n" \
                   "Drew a 5\n" \
                   "Dealer has 13.\n" \
                   "Drew a Queen\n" \
                   "Final hand: 23.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer_win_Blackjack_user_less_hand_value(self, input_mock, randint_mock):
        '''
        The dealer receives cards that end up with a hand of 21 and user hand less than 21.
        The dealer wins by having a higher hand than the user and hitting Blackjack.
        '''
        output = run_test([13, 11], ['n'], [1, 12], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a King\n" \
                   "Drew a Jack\n" \
                   "You have 20. Hit (y/n)? n\n" \
                   "Final hand: 20.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew a Queen\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer_win_user_Bust(self, input_mock, randint_mock):
        '''
        The dealer receive cards that end up with a hand of 21 and user hand more than 21.
        The dealer wins by hitting Blackjack and user Bust.
        '''
        output = run_test([3, 1, 13], ['y'], [1, 8], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew an Ace\n" \
                   "You have 14. Hit (y/n)? y\n" \
                   "Drew a King\n" \
                   "Final hand: 24.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew an 8\n" \
                   "Final hand: 19.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer_win_greater_value(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand less than 21.
        The dealer wins by having a higher hand than the user.
        '''
        output = run_test([1, 2, 4], ['y', 'n'], [4, 1, 4], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew a 2\n" \
                   "You have 13. Hit (y/n)? y\n" \
                   "Drew a 4\n" \
                   "You have 17. Hit (y/n)? n\n" \
                   "Final hand: 17.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 4\n" \
                   "Drew an Ace\n" \
                   "Dealer has 15.\n" \
                   "Drew a 4\n" \
                   "Final hand: 19.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_tie_both_Blackjack(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand of 21.
        Its a draw since both have the same total hand value and none of them bust.
        '''
        output = run_test([12, 5, 6], ['y'], [1, 13], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a Queen\n" \
                   "Drew a 5\n" \
                   "You have 15. Hit (y/n)? y\n" \
                   "Drew a 6\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew a King\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Push.\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_tie_both_same_hand_value_less_than_21(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand less than 21.
        It is a draw since they have the same total hand value.
        '''
        output = run_test([2, 6, 1], ['y', 'n'], [2, 11, 7], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 2\n" \
                   "Drew a 6\n" \
                   "You have 8. Hit (y/n)? y\n" \
                   "Drew an Ace\n" \
                   "You have 19. Hit (y/n)? n\n" \
                   "Final hand: 19.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 2\n" \
                   "Drew a Jack\n" \
                   "Dealer has 12.\n" \
                   "Drew a 7\n" \
                   "Final hand: 19.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Push.\n"
        self.assertEqual(output, expected)



if __name__ == '__main__':
    main()
