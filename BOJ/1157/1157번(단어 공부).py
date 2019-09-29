from sys import stdin


def solution(w):
    w = w.upper()
    if len(w) == 2:
        return w
    else:


        chk = dict()

        for i in range(0, len(w)):
            tmp = True
            if i == 0:
                chk[w[i]] = 1
            else:
                for k in chk.keys():
                    if w[i] == k:
                        chk[k] += 1
                        tmp = False

                if tmp == True:
                    chk[w[i]] = 1

        count = 0
        answerValue = 0

        for k in chk.keys():
            if chk[k] > answerValue:
                answerValue = chk[k]
                answerKey = k

        for k in chk.keys():
            if chk[k] == answerValue:
                count += 1

        if count >= 2:
            return '?'
        else:
            return answerKey


if __name__ == '__main__':
    word = stdin.readline()
    answer = solution(word)
    print(answer)
