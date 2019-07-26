import operator


def sort_voca(D):
    sorted_vocaList = sorted(D.items(), key=operator.itemgetter(0))
    sorted_vocaList.sort(key=operator.itemgetter(1))
    for t in sorted_vocaList:
        print(t[0])


if __name__ == '__main__':
    N = int(input())
    vocaList = dict()
    for i in range(N):
        voca = input()
        vl = len(voca)
        vocaList[voca] = vl
    sort_voca(vocaList)
