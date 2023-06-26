'''Калькулятор

Проверка решения
ID = 88565955'''


OPERATIONS: dict = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a // b
}


class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            return 'error'


def read_input() -> int:
    values = input().split()
    stack = Stack()
    for value in values:
        if value not in OPERATIONS:
            stack.push(int(value))
        else:
            operator_2 = stack.pop()
            operator_1 = stack.pop()
            result = OPERATIONS[value](operator_1, operator_2)
            stack.push(result)
    return stack.pop()


if __name__ == '__main__':
    print(read_input())
