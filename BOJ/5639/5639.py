import sys
sys.setrecursionlimit(10**6)


def printTree(start, end):
    if start > end:
        return

    division = end + 1
    for i in range(start + 1, end + 1):
        if answers[start] < answers[i]:
            division = i
            break
    printTree(start + 1, division - 1)
    printTree(division, end)
    print(answers[start])


answers = []
count = 0
while count <= 10000:
    try:
        num = int(int(sys.stdin.readline()))
    except:
        break
    answers.append(num)
    count += 1
printTree(0, len(answers) - 1)
