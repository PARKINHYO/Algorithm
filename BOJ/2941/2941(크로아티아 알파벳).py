from sys import stdin


def solution(w):
    ctAlphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
    split = []
    minus = 0

    for i in range(0, len(w) - 2):
        print(w[i:i + 3])
        for j in range(0, 8):

            if ctAlphabet[j] == w[i:i + 2] or ctAlphabet[j] == w[i:i + 3]:


                if w[i:i + 2] == 'z=':
                    if w[i - 1:i + 2] == 'dz=':
                        break

                split.append(ctAlphabet[j])

    tmpAnswer = 0
    for L in split:
        tmp = len(L)
        tmpAnswer += tmp

    answer = len(w) - 1 - tmpAnswer + len(split) - minus
    return answer


if __name__ == '__main__':
    CA = stdin.readline()
    answer = solution(CA)
    print(answer)
