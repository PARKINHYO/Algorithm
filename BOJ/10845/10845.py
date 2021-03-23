from sys import stdin
from collections import deque


class Queue:
    def __init__(self):
        self.queue = deque()

    def push(self, x):
        self.queue.append(x)

    def pop(self):
        return self.queue.popleft() if self.queue else -1

    def __sizeof__(self):
        return len(self.queue)

    def empty(self):
        return 0 if self.queue else 1

    def front(self):
        return self.queue[0] if self.queue else -1

    def back(self):
        return self.queue[-1] if self.queue else -1






q = Queue()
for i in range(int(stdin.readline())):
    cmd = stdin.readline().split()
    if cmd[0] == 'push':
        q.push(cmd[1])
    elif cmd[0] == 'pop':
        print(q.pop())
    elif cmd[0] == 'size':
        print(q.__sizeof__())
    elif cmd[0] == 'empty':
        print(q.empty())
    elif cmd[0] == 'front':
        print(q.front())
    elif cmd[0] == 'back':
        print(q.back())