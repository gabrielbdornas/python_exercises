import pytest
from list_google_foobar import solution

@pytest.mark.parametrize(
                          "list_, sum_, expect",
                          [
                           ([4, 3, 5, 7, 8], 12, [4, 3, 5]),
                           ([1, 2, 3, 4], 15, [-1, -1]),
                           ([12, 22, 3, 4], 7, [3, 4]),
                           ([12, 22, 3, 4, 7], 7, [3, 4]),
                           ([12, 1, 32, 3, 4, 7, 6, 22, 18], 20, [3, 4, 7, 6]),
                          ])
def test_solution_list_google_fooobar(list_, sum_, expect):
  assert solution(list_, sum_) == expect
