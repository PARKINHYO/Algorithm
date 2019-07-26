if __name__ == '__main__':
    N = int(input())
    AB = [[int(x) for x in input().split()] for y in range(N)]
    AB.sort()
    for i in range(N):
        for j in range(2):
            print(AB[i][j], end=' ')
        print()
