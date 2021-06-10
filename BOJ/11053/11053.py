import sys
input = sys.stdin.readline
import bisect

N = int(input())
prog = list(map(int, input().split()))
if N == 1:
    print(1)
    exit(0)
answers = [prog[0]]
for i in range(1, N):
    if answers[-1] < prog[i]:
        answers.append(prog[i])
    else:
        answers[bisect.bisect_left(answers, prog[i])] = prog[i]
print(len(answers))

