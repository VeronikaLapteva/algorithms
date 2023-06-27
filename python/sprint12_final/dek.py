'''Дек

Проверка решения
ID = 88568405'''


def SizeError(Exception):
    pass


class Dek:
    def __init__(self, m):
        self.__dek = [None] * m
        self.__max_m = m
        self.__head = 0
        self.__tail = 0
        self.__size = 0

    def is_empty(self):
        return self.__size == 0

    def is_overflow(self):
        return self.__size == self.__max_m

    def push_back(self, x):
        if self.is_overflow():
            return 'error'
        else:
            self.__dek[self.__tail] = x
            self.__tail = (self.__tail + 1) % self.__max_m
            self.__size += 1

    def push_front(self, x):
        if self.is_overflow():
            return 'error'
        else:
            self.__dek[self.__head - 1] = x
            self.__head = (self.__head - 1) % self.__max_m
            self.__size += 1

    def pop_front(self):
        if self.is_empty():
            return 'error'
        x = self.__dek[self.__head]
        self.__dek[self.__head] = None
        self.__head = (self.__head + 1) % self.__max_m
        self.__size -= 1
        return x

    def pop_back(self):
        if self.is_empty():
            return 'error'
        x = self.__dek[self.__tail - 1]
        self.__dek[self.__tail-1] = None
        self.__tail = (self.__tail - 1) % self.__max_m
        self.__size -= 1
        return x


def read_input():
    n: int = int(input())
    m: int = int(input())
    q = Dek(m)
    for _ in range(n):
        command, *values = input().split()
        try:
            result = getattr(q, command)(*values)
        except SizeError:
            result = 'error'
        if result is not None:
            print(result)


if __name__ == '__main__':
    read_input()
