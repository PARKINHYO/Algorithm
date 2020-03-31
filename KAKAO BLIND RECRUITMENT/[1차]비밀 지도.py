from sys import stdin


def solution(n, arr1, arr2):
    binarr1 = [""] * n
    binarr2 = [""] * n
    answer = [""] * n
    for i in range(n):
        binarr1[i] = bin(arr1[i])
        binarr1[i] = binarr1[i].replace("0b", "")
        binarr2[i] = bin(arr2[i])
        binarr2[i] = binarr2[i].replace("0b", "")

        if len(binarr1[i]) < n or len(binarr2[i]) < n:
            binarr1[i] = "0" * (n - len(binarr1[i])) + binarr1[i]
            binarr2[i] = "0" * (n - len(binarr2[i])) + binarr2[i]

        for j in range(n):
            if binarr1[i][j] == "0" and binarr2[i][j] == "0":
                answer[i] += " "
            else:
                answer[i] += "#"

    return answer


if __name__ == '__main__':
    n = int(stdin.readline())

    tmp1 = stdin.readline()
    tmp2 = stdin.readline()

    arr1 = list(map(int, tmp1.split(" ")))
    arr2 = list(map(int, tmp2.split(" ")))

    solution(n, arr1, arr2)
