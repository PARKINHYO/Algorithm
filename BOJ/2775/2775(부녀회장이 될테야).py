from sys import stdin


def solution(k, n):
    if n == 1:
        return 1
    if k == 0:
        return n

    else:
        return solution(k - 1, n) + solution(k, n - 1)


def solution2(k, n):
    tmpList = [[0 for i in range(15)] for j in range(15)]

    for i in range(0, len(tmpList[0])):
        tmpList[0][i] = i + 1
    for i in range(0, len(tmpList)):
        tmpList[i][0] = 1
    for i in range(1, k + 1):

        for j in range(1, n + 1):
            sum = 0
            for z in range(0, j + 1):
                sum += tmpList[i - 1][z]

            tmpList[i][j] = sum

    return tmpList[k][n - 1]


if __name__ == '__main__':
    T = int(stdin.readline())
    answer = []
    for i in range(0, T):
        k = int(stdin.readline())
        n = int(stdin.readline())
        answer.append(solution2(k, n))

    for L in answer:
        print(L)
