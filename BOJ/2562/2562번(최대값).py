from sys import stdin


def Max_Number(l):
    tmp = sdfasdfl.copy()
    tmp.sort()
    for i in range(9):
        if l[i] == tmp[8]:
            answer = i

    print(tmp[8])
    print(answer + 1)


if __name__ == '__main__':
    my_list = []
    for i in range(9):
        n = int(stdin.readline())
        my_list.append(n)

    Max_Number(my_list)
