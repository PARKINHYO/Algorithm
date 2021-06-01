import sys
input = sys.stdin.readline

scores = []
for _ in range(int(input())):
    name, kor, eng, math = input().split()
    kor, eng, math = int(kor), int(eng), int(math)
    scores.append([name, kor, eng, math])

scores.sort(key=lambda x : (-x[1], x[2], -x[3], x[0]))
for scores in scores:
    print(scores[0])