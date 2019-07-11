score = []
sum=0
for i in range(5):
    score.append(int(input()))
    if score[i]<40:
        score[i]=40
    sum+=score[i]
average = sum/5
print(int(average))