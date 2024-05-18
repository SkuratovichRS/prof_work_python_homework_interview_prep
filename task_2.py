from task_1 import Stack


def balanced_parentheses(parentheses: str) -> bool:
    stack = Stack()
    pairs = {")": "(", "]": "[", "}": "{"}
    for p in parentheses:
        if p not in pairs:
            stack.push(p)
        else:
            if stack.is_empty():
                return False
            if pairs[p] != stack.peek():
                return False
            stack.pop()

    return True if stack.is_empty() else False


print(balanced_parentheses("([])((([[[]]])))]{()}"))