from sys import stdin

a, b = map(int, stdin.readline().split())
A = a
B = b
GCD = 0
LCM = 0

while True:
    r = a % b

    if r == 0:
        GCD = b
        break

    a = b
    b = r

LCM = (A/GCD) * (B/GCD) * GCD
print(GCD, "%d" % LCM)

