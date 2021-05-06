import sys

n = int(sys.stdin.readline())
mylist = [x for x in range(1, n+1)]
last = 0
stack = []
answer = ''
program = True
problem = []
for _ in range(n):
    problem.append(int(sys.stdin.readline()))
    
for i in range(n):
    if not mylist and problem[i] > last:
        program = False
        break
    if problem[i] > last:
        while True:
            tmp = mylist.pop(0)
            stack.append(tmp)
            answer += "+\n"
            if tmp == problem[i]:
                break
    if not stack:
        program = False
        break
    if stack.pop() != problem[i]:
        program = False
        break
    answer += "-\n"
    last = problem[i]

if program:
    print(answer)
else:
    print("NO")
