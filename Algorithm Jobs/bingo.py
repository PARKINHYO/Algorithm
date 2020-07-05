from sys import stdin

global count

def logic2(n, M):
    global count
    count = 0
    for i in range(5):
        for j in range(5):
            if M[i][j] == n:
                M[i][j] = 0

    for i in range(5):
        garo = True
        for j in range(5):
            if M[i][j] != 0:
                garo = False
        if garo == True:
            if count == 3:
                return
            count += 1

    for i in range(5):
        saro = True
        for j in range(5):
            if M[j][i] != 0:
                saro = False
        if saro == True:
            if count == 3:
                return
            count += 1

    dagaksun1 = True
    for i in range(5):
        if M[i][i] != 0:
            dagaksun1 = False
    if dagaksun1 == True:
        if count == 3:
            return
        count += 1

    dagaksun2 = True
    for i in range(5):
        if M[i][4 - i] != 0:
            dagaksun2 = False
    if dagaksun2 == True:
        if count == 3:
            return
        count += 1

    return


def logic1(M, N):
    global count

    for i in range(5):
        for j in range(5):
            logic2(N[i][j], M)
            if count == 3:
                return


if __name__ == '__main__':

    M = []
    N = []

    for i in range(5):
        tmp = list(map(int, stdin.readline().split()))
        M.append(tmp)
    for i in range(5):
        tmp = list(map(int, stdin.readline().split()))
        N.append(tmp)


    logic1(M, N)
    answer = 0
    for i in range(5):
        for j in range(5):
            if M[i][j] == 0:
                answer += 1
    print(answer)
