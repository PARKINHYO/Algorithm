import sys
input = sys.stdin.readline
N = input().rstrip()
if '0' not in N:
    print(-1)
    exit(0)
if int(N) % 3 != 0:
    print(-1)
    exit(0)
answer = list(N)
answer.sort(reverse=True)
print(''.join(answer))