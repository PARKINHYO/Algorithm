S = int(input())
R = [[x for x in input().split()] for y in range(S)]
word=""
word2=""
word3=""
for i in range(S):
    word = R[i][1]
    for j in range(len(word)):
        word2 = word[j]*int(R[i][0])
        word3+=word2
    print(word3)
    word3=""