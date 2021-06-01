import sys
input = sys.stdin.readline

N, K = map(int, input().split())
print(sorted(list(map(int, input().split())))[K-1])