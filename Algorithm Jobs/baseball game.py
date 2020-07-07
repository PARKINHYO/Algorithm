from sys import stdin


class baseballGame:

    def logic2(self, n2, n):

        tmp1 = list(n2)
        tmp2 = list(n)

        strike = 0
        ball = 0
        for i in range(3):
            if tmp1[i] == tmp2[i]:
                strike += 1
            elif tmp2[i] in tmp1:
                ball += 1

        return tuple(str(strike) + str(ball))

    def logic(self, hints):
        lists = list(filter(lambda x: len(set(x)) == 3,
                            [str(x) + str(y) + str(z) for x in range(1, 10) for y in range(1, 10) for z in
                             range(1, 10)]))
        answer = []
        for n in lists:
            tmp = 0
            for h in hints:
                h = h.split()

                # print(type(self.logic2(n, h[0])))
                # print(type((h[1], h[2])))
                # print(type(n))
                # print(type(h[0]))
                # print(type(h[1]))
                # print(type(h[2]))
                if self.logic2(n, h[0]) == (h[1], h[2]):
                    tmp += 1

            if tmp == len(hints):
                answer.append(n)
        return answer


if __name__ == '__main__':
    hints = []
    for i in range(int(stdin.readline())):
        hints.append(input())
    n = baseballGame()
    print(len(n.logic(hints)))
