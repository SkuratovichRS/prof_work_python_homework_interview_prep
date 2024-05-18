from typing import Any


class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self) -> bool:
        return True if not self.stack else False

    def push(self, element: Any) -> None:
        self.stack.append(element)

    def pop(self) -> Any:
        return self.stack.pop()

    def peek(self) -> Any:
        return self.stack[-1]

    def size(self) -> int:
        return len(self.stack)



