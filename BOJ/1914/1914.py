def hanoi(n, from_pos, to_pos, aux_pos):
    if n == 1:
        print(str(from_pos) + " " + str(to_pos))
        return

    hanoi(n - 1, from_pos, aux_pos, to_pos)
    print(str(from_pos) + " " + str(to_pos))
    hanoi(n - 1, aux_pos, to_pos, from_pos)


N = int(input())
if N > 20:
    print(pow(2, N) - 1)
else:
    print(pow(2, N) - 1)
    hanoi(N, 1, 3, 2)