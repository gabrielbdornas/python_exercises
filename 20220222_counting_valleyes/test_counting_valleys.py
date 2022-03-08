import pytest
from counting_valleys import solution

@pytest.mark.parametrize(
                          "steps, path, expect",
                          [
                           (8, 'UDDDUDUU', 1),
                           (4, 'DUDU', 2),
                           (7, 'DUUUUDD', 1),
                          ])
def test_solution_list_google_fooobar(steps, path, expect):
  assert solution(steps, path) == expect
