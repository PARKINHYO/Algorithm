def find_same_name(n, a):
    # name_dict = {}
    for number in a:
        if number == n:
            return a[number]

    return "?"


name = {39: "Justin", 14: "John", 67: "Mike", 105: "Summer"}

while True:
    N = int(input())
    print(find_same_name(N, name))
