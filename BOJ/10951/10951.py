while True:
    try:
        AB = [int(x) for x in input().split()]
        print(AB[0] + AB[1])
    except EOFError:
        break