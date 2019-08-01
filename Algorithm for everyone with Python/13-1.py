def print_all_friends(g, start):
    qu = []
    done = set()

    qu.append(start)
    done.add(start)

    p = qu[0]

    while g[p][0]:
        g[p][0] = g[p][0][0]

        if g[p] not in done:
            qu.append(g[p])
            done.add(g[p])


fr_info = {
    1: [2, 3],
    2: [4, 5],
    3: [],
    4: [],
    5: []
}


print(fr_info[fr_info[1][0]][0])
#print(print_all_friends(fr_info, 1))
