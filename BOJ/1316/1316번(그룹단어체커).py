from sys import stdin


def solution(ws):
    count = 0

    for s in range(0, len(ws)):
        check = []
        GW = True
        for i in range(0, len(ws[s])):
            if len(ws[s]) == 1 or len(ws[s]) == 2:
                break
            if i == 0:
                check.append(ws[s][i])
            else:
                if ws[s][i] != ws[s][i - 1]:
                    for j in range(0, len(check)):
                        if ws[s][i] == check[j]:
                            GW = False
                            # check.append(ws[s][i])

                    check.append(ws[s][i])

        if GW == True:
            count += 1

    return count


if __name__ == '__main__':

    N = int(stdin.readline())
    words = []

    for i in range(0, N):
        word = stdin.readline()
        words.append(word)

    answer = solution(words)
    print(answer)
