class StackEmptyError(Exception):
    pass


class StackOverflowError(Exception):
    pass


class Stack:
    def __init__(s, capacity):
        s.capacity = capacity
        s.items = []

    def push(s, item):
        if len(s.items) >= s.capacity:
            raise StackOverflowError("Stack is full")
        s.items.append(item)

    def pop(s):
        if not s.items:
            raise StackEmptyError("Stack is empty")
        return s.items.pop()


stack = Stack(2)

try:
    stack.pop()
except StackEmptyError as e:
    print("Caught StackEmptyError:", e)
finally:
    print("thank you!")
try:
    stack.push(10)
    stack.push(20)
    stack.push(30)
except StackOverflowError as e:
    print("Caught StackOverflowError:", e)
finally:
    print("thank you!")    