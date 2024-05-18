import pytest
from task_2 import balanced_parentheses


@pytest.mark.parametrize(
    "parentheses, expected",
    (
            ["(((([{}]))))", True],
            ["[([])((([[[]]])))]{()}", True],
            ["{{[()]}}", True],
            ["}{}", False],
            ["{{[(])]}}", False],
            ["[[{())}]", False]
    )
)
def test_balanced_parentheses(parentheses: str, expected: bool) -> None:
    actual = balanced_parentheses(parentheses)
    assert actual == expected
