from sys import stdin

if __name__ == '__main__':
    C = int(stdin.readline())
    answers = []
    for i in range(0, C):
        case = list(map(int, stdin.readline().split()))
        sum = 0
        for j in range(1, len(case)):
            sum += case[j]

        average = sum / case[0]
        count = 0
        for j in range(1, len(case)):
            if average < case[j]:
                count += 1

        answer = float(count / case[0] * 100)
        answers.append(answer)

    for L in answers:
        print('%.3f' % L, end="")
        print("%")
