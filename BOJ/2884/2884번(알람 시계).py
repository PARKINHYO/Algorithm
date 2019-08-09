from sys import stdin


def Alarm(l):
    if l[1] < 45:
        l[1] += 15
        l[0] -= 1
        if l[0] == -1:
            l[0] += 24
    else:
        l[1] -= 45

    return l


if __name__ == '__main__':
    HM = list(map(int, stdin.readline().split()))
    answer = Alarm(HM)
    for l in answer:
        print(l, end=' ')
