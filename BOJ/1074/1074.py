import sys

count = 0


def cur(n, x, y):
    global count
    if x == r and y == c:
        print(int(count))
        exit(0)
    if n == 1:
        count += 1
        return
    if not (x <= r < x+n and y <= c < y+n):
        count += n*n
        return
    cur(n/2, x, y)
    cur(n/2, x, y+n/2)
    cur(n/2, x+n/2, y)
    cur(n/2, x+n/2, y+n/2)


N, r, c = map(int,sys.stdin.readline().split())
cur(2**N,0,0)
