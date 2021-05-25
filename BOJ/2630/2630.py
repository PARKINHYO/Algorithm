import sys


def sameColor(n,x,y):
    global answerBlue
    global answerWhite
    white, blue = 0,0
    for i in range(x, x+n):
        for j in range(y, y+n):
            if paper[i][j] == 0:
                white +=1
            else:
                blue += 1
    if white == n*n:
        answerWhite += 1
        return True
    elif blue == n*n:
        answerBlue += 1
        return True
    else: 
        return False


def cur(n, x, y):
    
    if sameColor(n,x,y):
        return

    cur(n//2, x, y)
    cur(n//2, x + n//2, y)
    cur(n//2, x, y + n//2)
    cur(n//2, x + n//2, y + n//2)


N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
answerWhite = 0
answerBlue = 0
cur(N,0,0)
print(answerWhite)
print(answerBlue)