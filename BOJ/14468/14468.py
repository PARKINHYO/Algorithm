import sys
input = sys.stdin.readline

cows = input().rstrip()

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

count =0
for i in range(len(alphabet)):
    for j in range(i+1, len(alphabet)):
        cur = [x for x, value in enumerate(cows) if value == alphabet[i]]
        if cows[cur[0]+1:cur[1]].count(alphabet[j]) == 1:
            count += 1
print(count)