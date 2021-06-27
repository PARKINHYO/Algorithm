import sys, collections
input = sys.stdin.readline

Q = collections.deque([x for x in range(1, int(input())+1)])

while True: 
    if len(Q) == 1:
        print(Q.pop())
        break
    Q.popleft()
    Q.append(Q.popleft())
