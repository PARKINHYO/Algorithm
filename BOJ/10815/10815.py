import sys
import bisect


N = int(sys.stdin.readline())
mycards = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
mycards.sort()
answers = []
for card in cards:
    index = bisect.bisect_left(mycards, card)
    if index < N and mycards[index] == card:
        answers.append(1)
    else:
        answers.append(0)
    

print(*answers) 