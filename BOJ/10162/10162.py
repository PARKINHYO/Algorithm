import sys


T = int(sys.stdin.readline())
buttons = [300,60,10]
answer = []
for button in buttons:
    answer.append(T // button)
    T %= button
if T != 0:
    print(-1)
else:
    print(*answer)