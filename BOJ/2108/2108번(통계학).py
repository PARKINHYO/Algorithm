from sys import stdin
import math

def average(l):
    sum = 0
    for i in range(len(l)):
        sum += list[i]
    ar = sum / len(l)
    if (abs(ar - round(ar)) == 0.5 and math.trunc(ar) % 2 == 0):
        if (ar < 0):
            return round(ar) - 1
        else:
            return round(ar) + 1

    return round(ar)


def median(l):
    l.sort()
    tmp = len(l) // 2
    return l[tmp]


def mode(l):
    n = len(l)
    sample_answer = dict()
    for i in range(-4000, 4001):
        sample_answer[i] = 0
    count = 0
    for i in range(n):
        sample_answer[l[i]] += 1
        if sample_answer[l[i]] > count:
            count = sample_answer[l[i]]

    answer = []
    for keys in sample_answer:
        if sample_answer[keys] == count:
            answer.append(keys)

    answer.sort()
    if len(answer) == 1:
        return answer[0]
    else:
        return answer[1]


def Range(l):
    l.sort()
    return l[len(l) - 1] - l[0]


if __name__ == '__main__':
    N = int(stdin.readline())
    list = []
    for i in range(N):
        n = int(stdin.readline())
        list.append(n)

    print(average(list))
    print(median(list))
    print(mode(list))
    print(Range(list))
