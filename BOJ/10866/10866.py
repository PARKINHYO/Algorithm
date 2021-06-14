import sys
input = sys.stdin.readline
import collections


class Solution:
    def __init__(self):
        self.Q = collections.deque([])
    
    
    def push_front(self, X):
        self.Q.appendleft(X)
    
    
    def push_back(self, X):
        self.Q.append(X)
        
    
    def pop_front(self):
        if self.Q:
            print(self.Q.popleft())
        else:
            print(-1)
    
    
    def pop_back(self):
        if self.Q:
            print(self.Q.pop())
        else:
            print(-1)
            
        
    def size(self):
        print(len(self.Q))
    
    
    def empty(self):
        if self.Q:
            print(0)
        else:
            print(1)
    
    
    def front(self):
        if self.Q:
            print(self.Q[0])
        else:
            print(-1)

    
    def back(self):
        if self.Q:
            print(self.Q[-1])
        else:
            print(-1)

s = Solution()
for _ in range(int(input())):
    func = input().rstrip()
    if ' ' in func:
        func, arg = func.split()
        if func == 'push_front':
            s.push_front(arg)
        elif func == 'push_back':
            s.push_back(arg)
    else:
        if func == 'pop_front':
            s.pop_front()
        elif func == 'pop_back':
            s.pop_back()
        elif func == 'size':
            s.size()
        elif func == 'empty':
            s.empty()
        elif func == 'front':
            s.front()
        elif func == 'back':
            s.back()