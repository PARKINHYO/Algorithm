number = [int(i) for i in input()]
number.sort()
number.reverse()
for i in range(len(number)):
    print(number[i], end="")