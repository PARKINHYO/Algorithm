from sys import stdin
import copy


def Stksystem(d, g):
    stk = []
    rule = {0: 1, 1: 2, 2: 3, 3: 0}
    stk.append(d)
    if g >= 1:
        for i in range(0, g):
            tmp = copy.deepcopy(stk)
            for j in range(0, 2 ** i):
                stk.append(rule[tmp.pop()])

    return stk


def Solution(n, str2):
    bool = False
    xy = []
    for i in range(0, n):
        x = str2[i][0]
        y = str2[i][1]
        d = str2[i][2]
        g = str2[i][3]

        X = {0: 1, 1: 0, 2: -1, 3: 0}
        Y = {0: 0, 1: -1, 2: 0, 3: 1}

        xy.append([x, y])

        stk = Stksystem(d, g)
        for l in stk:
            x += X[l]
            y += Y[l]
            xy.append([x, y])

    xy.sort()
    tmp = []

    for i in range(0, len(xy) - 1):
        if xy[i] == xy[i + 1]:
            tmp.append(xy[i])
    for i in range(0, len(tmp)):
        xy.remove(tmp[i])

    answer = 0
    for i in range(0, len(xy)):
        right = False
        below = False
        diag = False
        for j in range(0, len(xy)):
            if xy[j][0] == xy[i][0] + 1 and xy[j][1] == xy[i][1]:
                right = True
            if xy[j][0] == xy[i][0] and xy[j][1] == xy[i][1] + 1:
                below = True
            if xy[j][0] == xy[i][0] + 1 and xy[j][1] == xy[i][1] + 1:
                diag = True

        if right == True and below == True and diag == True:
            answer += 1
    return answer


if __name__ == '__main__':
    N = int(stdin.readline())
    info = []
    answer = 0
    for i in range(0, N):
        tmp = []
        tmp = list(map(int, stdin.readline().split()))
        info.append(tmp)

    answer = Solution(N, info)
    print(answer)
