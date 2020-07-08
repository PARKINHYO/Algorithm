from sys import stdin


data = list(map(int, stdin.readline().split()))

for i in range(len(data)):
    inx = i
    for j in range(i, len(data)):
        if data[inx] > data[j]:
            inx = j

    temp = data[i]
    data[i] = data[inx]
    data[inx] = temp
    for j in range(len(data)):
        print(data[j], end=" ")
    print()

# for i in range(len(data)):
#     print(data[i], end=" ")

