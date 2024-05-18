import pytest
from task_1 import Stack


class TestTask1:
    def setup_method(self):
        self.stack = Stack()

    @pytest.mark.parametrize(
        "stack, expected",
        (
                [[1, 2, 3], False],
                [[], True]
        )
    )
    def test_is_empty(self, stack: list, expected: bool) -> None:
        self.stack.stack += stack
        actual = self.stack.is_empty()
        assert actual == expected

    def test_push(self) -> None:
        self.stack.stack += [1, 2, 3]
        self.stack.push(4)
        actual = self.stack.stack[-1]
        expected = 4
        assert actual == expected

    def test_pop(self) -> None:
        self.stack.stack += [1, 2, 3]
        actual = self.stack.pop()
        expected = 3
        assert actual == expected

    def test_peek(self) -> None:
        self.stack.stack += [1, 2, 3]
        actual = self.stack.peek()
        expected = 3
        assert actual == expected

    def test_size(self) -> None:
        self.stack.stack += [1, 2, 3]
        actual = self.stack.size()
        expected = 3
        assert actual == expected
