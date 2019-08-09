import calendar
from sys import stdin


def leaf(y):
    if (y % 4 == 0) and (y % 100 != 0) or y % 400 == 0:
        print(1)
    else:
        print(0)


if __name__ == '__main__':
    year = int(stdin.readline())
    leaf(year)
x