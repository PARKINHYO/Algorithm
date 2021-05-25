import sys


money = 1000 - int(sys.stdin.readline())

changes = [500,100,50,10,5,1]
answer = 0
for change in changes:
     answer += money//change
     money %= change
print(answer)
