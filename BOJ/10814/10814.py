from sys import stdin
import operator


def solution(m):
    sorted_x = sorted(m, key=operator.itemgetter(0))
    for l in sorted_x:
        print(l[0], l[1])


if __name__ == '__main__':

    N = int(stdin.readline())
    member = []
    for i in range(0, N):
        tmp = list(stdin.readline().split())
        tmp[0] = int(tmp[0])
        member.append(tmp)

    solution(member)
