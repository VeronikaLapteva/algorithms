COMMANDS: set = (
    'push_back',
    'push_front',
    'pop_front',
    'pop_back'
)


class Dek:
    def __init__(self, m):
        self.dek = [None] * m
        self.max_m = m
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        if self.size == 0:
            return True

    def is_overflow(self):
        if self.size == self.max_m:
            return True

    def push_back(self, x):
        if self.is_overflow():
            print('error')
        else:
            self.dek[self.tail] = x
            self.tail = (self.tail + 1) % self.max_m
            self.size += 1

    def push_front(self, x):
        if self.is_overflow():
            print('error')
        else:
            self.dek[self.head - 1] = x
            self.head = (self.head - 1) % self.max_m
            self.size += 1

    def pop_front(self):
        if self.is_empty():
            return 'error'
        x = self.dek[self.head]
        self.dek[self.head] = None
        self.head = (self.head + 1) % self.max_m
        self.size -= 1
        return x

    def pop_back(self):
        if self.is_empty():
            return 'error'
        x = self.dek[self.tail - 1]
        self.dek[self.tail-1] = None
        self.tail = (self.tail - 1) % self.max_m
        self.size -= 1
        return x


def read_input():
    n: int = int(input())
    m: int = int(input())
    q = Dek(m)
    for i in range(n):
        command = input().split()
        if command[0] == 'push_back':
            q.push_back(int(command[1]))
        elif command[0] == 'push_front':
            q.push_front(int(command[1]))
        elif command[0] == 'pop_front':
            print(q.pop_front())
        elif command[0] == 'pop_back':
            print(q.pop_back())


if __name__ == '__main__':
    read_input()
