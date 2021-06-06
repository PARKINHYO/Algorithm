import sys
input = sys.stdin.readline


def productMatrix(arr1, arr2):
    answer = []
    for idx1 in range(len(arr1)):
        row = []
        for idx2 in range(len(arr2[0])):
            tmp = 0
            for idx3 in range(len(arr1[0])):
                tmp += arr1[idx1][idx3] * arr2[idx3][idx2]
            row.append(tmp)
        answer.append(row)
    return answer

N, M = map(int, input().split())
arr1 = [list(map(int, input().split())) for _ in range(N)]
N, M = map(int, input().split())
arr2 = [list(map(int, input().split())) for _ in range(N)]

answer = productMatrix(arr1, arr2)
for a in answer:
    print(*a)
