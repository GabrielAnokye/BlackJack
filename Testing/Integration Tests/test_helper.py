from importlib import reload
import io
import sys

def print_value(question, answer):
    print(question + answer)
    return answer

def run_test(user_cards, answers, dealer_cards, randint_mock, input_mock):
    """
    Mocks randint and runs function with mock

    Args:
      randint_mock - patched random.randint()
      cards - desired input for random.randint()
      input_mock - patched bultins.input()
      answers - desired input for builtins.input()
      imported - whether module was imported already; always pass in True for your tests
    """
    answers.reverse() # reverses answers so can pop off list
    randint_mock.side_effect = user_cards + dealer_cards # set randint calls to cards
    input_mock.side_effect = \
        lambda question: print_value(question, answers.pop()) # print input question along with given answer

    # Save printed output into variable so can return it to compare in test
    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout
    imported = 'blackjack' in sys.modules
    import blackjack
    if imported:
        reload(blackjack)
    output = new_stdout.getvalue()
    sys.stdout = old_stdout
    return output # return printed statements in student-run code
