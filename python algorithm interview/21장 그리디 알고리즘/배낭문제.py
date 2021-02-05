
def fractional_knapsack(cargo):
    capacity = 15
    pack = []
    # 단가 계산 역순 정렬
    for c in cargo:
        pack.append((c[0] / c[1], c[0], c[1]))

    pack.sort(reverse=True)

    # 단가 순 그리디 계산
    total_value: float = 0
    for p in pack:
        if capacity - p[2] >= 0:
            capacity -= p[2]
            total_value += p[1]
        else:
            fraction = capacity / p[2]
            total_value += p[1] * fraction
            break

    return total_value