import sys
import collections

celledBook = collections.defaultdict(int)
for _ in range(int(sys.stdin.readline())):
    celledBook[sys.stdin.readline().rstrip()] += 1
tmp = collections.Counter(celledBook).most_common()
k = tmp[0][1]
answers = []
for t in tmp:
    if t[1] == k:
        answers.append(t)
answers.sort(key=lambda x: x[0])
print(answers[0][0])

