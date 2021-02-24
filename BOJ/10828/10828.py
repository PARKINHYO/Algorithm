import collections
from sys import stdin


class Solution:
    def __init__(self):
        self.stack = collections.deque()

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        return self.stack.pop() if self.stack else -1

    def size(self):
        return len(self.stack)

    def empty(self):
        return 0 if self.stack else 1

    def top(self):
        return self.stack[-1] if self.stack else -1


N = int(stdin.readline())
s = Solution()
answer = ''
for i in range(N):
    cmd = stdin.readline()
    if ' ' in cmd:
        func, arg = cmd.split()
        s.push(int(arg))

    if cmd == 'pop\n':
        answer += str(s.pop()) + '\n'
    elif cmd == 'size\n':
        answer += str(s.size()) + '\n'
    elif cmd == 'empty\n':
        answer += str(s.empty()) + '\n'
    elif cmd == 'top\n':
        answer += str(s.top()) + '\n'
    else:
        pass
print(answer)
