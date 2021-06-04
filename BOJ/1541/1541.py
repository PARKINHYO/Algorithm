import sys
input = sys.stdin.readline

exps = input().strip().split('-')

answers_to_subtract = []
for e in exps:
    nums = e.split('+')
    tmp = 0
    for n in nums:
        tmp += int(n)
    answers_to_subtract.append(tmp)
answer = answers_to_subtract[0]
for i in range(1, len(answers_to_subtract)):
    answer -= answers_to_subtract[i]
print(answer)