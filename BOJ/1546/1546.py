N = int(input())
score = []
score = input().split()
score = [int (i) for i in score]
score.sort()

for i in range(0, N-1):
    score[i] = float(score[i])/float(score[N-1])*100

score[N-1] = 100
sum = 0
for i in range(0, N):
    sum += float(score[i])

average = float(sum)/N
if len(str(average))>=10:
    print("%0.6f" % average)
else:
    print("%0.2f" % average)