from sys import stdin


def compare(l):
    if l[0] < l[1]:
        print('<')
    elif l[0] > l[1]:
        print('>')
    else:
        print('==')


if __name__ == '__main__':
    AB = list(map(int, stdin.readline().split()))
    compare(AB)
