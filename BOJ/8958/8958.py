from sys import stdin

def solution(a):
    answers = []
    for i in range(0, len(a)):
        answer = 0
        count = 0
        for j in range(0, len(a[i])):
            if a[i][j] == 'O':
                count += 1
                answer += count
            else:
                count = 0
        answers.append(answer)

    return  answers



if __name__ == '__main__':
    n = int(stdin.readline())
    results = []
    for i in range(0, n):
        results.append(stdin.readline())

    answers = solution(results)

    for L in answers:
        print(L)
