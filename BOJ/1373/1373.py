import sys
input = sys.stdin.readline
n = int('0b' + input().rstrip(), 2)

if n >= 0:
    print(str(oct(n))[2:])
else:
    tmp = str(oct(abs(n) + 1))[2:]
    answer = ''
    for t in tmp:
        if t == '0':
            answer += '1'
        else:
            answer += '0'
    print(int(answer))

