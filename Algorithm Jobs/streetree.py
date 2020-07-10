from sys import stdin


# 2 | 2 4 6
#   -------
#     1 2 3

def GCD(x, y):
    if x > y:
        a = x
        b = y
    else:
        a = y
        b = x

    while True:
        r = a % b
        if r == 0:
            break
        a = b
        b = r
    return b


if __name__ == '__main__':

    G = []
    for i in range(int(stdin.readline())):
        G.append(int(stdin.readline()))
    btwG = []
    for i in range(len(G) - 1):
        btwG.append(G[i + 1] - G[i])
    while True:
        if len(btwG) == 1:
            break
        a = btwG.pop()
        b = btwG.pop()
        r = GCD(a, b)
        btwG.append(r)
    print((G.pop() - G[0]) // btwG[0] - len(G))
