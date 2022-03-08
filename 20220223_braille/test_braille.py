import pytest
from braille import solution

@pytest.mark.parametrize(
                          "word, expect",
                          [
                           ('Braille', '000001110000111010100000010100111000111000100010'),
                           ('Gabriel', '000001110110100000110000111010010100100010111000'),
                          ])
def test_solution_list_google_fooobar(word, expect):
  assert solution(word) == expect
