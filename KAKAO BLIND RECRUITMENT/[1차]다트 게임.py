from sys import stdin
import re


def solution(score):
    regex = re.compile("\d+\w[*#]|\d+\w")
    chance = regex.findall(score)

    paper = [0] * 3
    option = [" "] * 3
    for i in range(3):
        regex2 = re.compile("\d+|\w|[*#]")
        detachan = regex2.findall(chance[i])

        if detachan[1] == 'S':
            paper[i] = int(detachan[0])

        elif detachan[1] == 'D':
            paper[i] = int(detachan[0]) ** 2
        else:
            paper[i] = int(detachan[0]) ** 3

        if len(detachan) == 3:
            option[i] = detachan[2]

    count = 0
    for i in range(3):

        if option[i] == '*':
            if i == 0:
                paper[i] *= 2
            else:
                for j in range(i, i - 2, -1):
                    paper[j] *= 2
            if count == 1:
                for j in range(i - 1, -1, -1):
                    if paper[j] == '*':
                        paper[j] *= 2
                    elif paper[j] == '#':
                        paper[j] *= 2
                    else:
                        continue
            count = 1

        elif option[i] == '#':
            paper[i] = -paper[i]
            if count == 1:
                for j in range(i - 1, -1, -1):
                    if paper[j] == '*':
                        paper[j] *= 2
                    elif paper[j] == '#':
                        paper[j] *= 2
                    else:
                        continue
            count = 1

        else:
            continue

    answer = 0
    for l in paper:
        answer += l

    return answer


if __name__ == '__main__':
    score = stdin.readline()
    solution(score)
