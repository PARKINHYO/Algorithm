import sys


class Solution:
    def __init__(self):
        self.s = set()

    def add(self, x):
        if x not in self.s:
            self.s.add(x)

    def remove(self, x):
        if x in self.s:
            self.s.remove(x)

    def check(self, x):
        if x in self.s:
            print(1)
        else:
            print(0)

    def toggle(self, x):
        if x in self.s:
            self.s.remove(x)
        else:
            self.s.add(x)

    def all(self):
        self.s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                  11, 12, 13, 14, 15, 16, 17, 18, 19, 20}

    def empty(self):
        self.s = set()


s = Solution()
for _ in range(int(sys.stdin.readline())):
    tmp = sys.stdin.readline().rstrip()

    if ' ' in tmp:
        func, arg = tmp.split()
        if func == 'add':
            s.add(int(arg))
        elif func == 'remove':
            s.remove(int(arg))
        elif func == 'check':
            s.check(int(arg))
        else:
            s.toggle(int(arg))
    else:
        if tmp == 'all':
            s.all()
        else:
            s.empty()
