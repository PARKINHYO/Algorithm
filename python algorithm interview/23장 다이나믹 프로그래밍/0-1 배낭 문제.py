def zero_one_knapsack(cargo):
    capacity = 15
    pack = []

    for i in range(len(cargo) + 1):
        pack.append([])
        for c in range(capacity + 1):
            # fixme 가로와 세로의 첫줄을 다 0으로 채움.
            if i == 0 or c == 0:
                pack[i].append(0)
            # fixme 짐 개수가 1개 이상이고, 배낭 용량도 1개 이상일 때
            # fixme i는 1부터 시작하므로 cargo에서 처음부터 확인하려면 cargo[i-1][1]으로 kg을 가지고 와서
            # fixme 현재 capacity보다 작거나 같을 때 가방에 넣을지 말지 결정한다.
            elif cargo[i - 1][1] <= c:
                pack[i].append(
                    max(
                        # fixme cargo에서 달러 +
                        # fixme 짐의 개수가 하나 전일 때(i-1),
                        # fixme 현재 capacity c 에서 지금 들어가려는 짐의 capacity인 cargo[i-1][1]를 뺀 capacity 부분의 가치를 확인해서 둘이 더함.
                        cargo[i - 1][0] + pack[i - 1][c - cargo[i - 1][1]],
                        # fixme 전의 값과 비교해서 더 큰 값을 선택
                        pack[i - 1][c]
                    ))
            else:
                # fixme. 아니면 전꺼 그대로 추가
                pack[i].append(pack[i - 1][c])

    return pack[-1][-1]


cargo = [
    (4, 12),
    (2, 1),
    (10, 4),
    (1, 1),
    (2, 2),
]

print(zero_one_knapsack(cargo))

