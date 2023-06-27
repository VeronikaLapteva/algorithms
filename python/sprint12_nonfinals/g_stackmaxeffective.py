class StackMaxEffective:
    def __init__(self):
        self.items = []
        self.g_max = []

    def push(self, item):
        if len(self.items) == 0 or item >= self.g_max[-1]:
            self.g_max.append(item)
        self.items.append(item)

    def pop(self):
        if len(stack.items) == 0:
            return 'error'
        if self.items.pop() == self.g_max[-1]:
            self.g_max.pop()

    def get_max(self):
        if len(self.items) == 0:
            return 'None'
        return self.g_max[-1]


stack = StackMaxEffective()
number = int(input())
answer = []
for _ in range(number):
    input_commands = input().split()
    if input_commands[0] == "push":
        stack.push(int(input_commands[1]))
    if input_commands[0] == "pop":
        if stack.pop() == 'error':
            answer.append('error')
    if input_commands[0] == "get_max":
        answer.append(stack.get_max())
for i in answer:
    print(i)
