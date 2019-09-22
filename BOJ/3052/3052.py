from sys import stdin


def solution(s):
    count = 1

    for i in range(1, 10):
        same = False
        for j in range(0, i):
            if s[i] == s[j]:
                same = True

        if same == False:
            count += 1

    return count


if __name__ == '__main__':
    numbers = []
    for i in range(0, 10):
        tmp = int(stdin.readline())%42
        numbers.append(tmp)

    answer = solution(numbers)
    print(answer)
