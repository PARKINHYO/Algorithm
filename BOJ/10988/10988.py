import sys
input = sys.stdin.readline

s = input().rstrip()

if s == s[::-1]:
    print(1)
else:
    print(0)
    