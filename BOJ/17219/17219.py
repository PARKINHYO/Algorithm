import sys, collections
input = sys.stdin.readline


users = collections.defaultdict(str)
N, M = map(int, input().split())
for _ in range(N):
    site, passwd = input().split()
    users[site] = passwd
for _ in range(M):
    print(users[input().rstrip()])
    