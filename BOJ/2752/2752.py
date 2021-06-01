import sys
input = sys.stdin.readline

print(*sorted(list(map(int, input().split()))))