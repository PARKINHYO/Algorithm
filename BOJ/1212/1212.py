import sys
input = sys.stdin.readline
n = int('0o' + input().rstrip(), 8)

if n >= 0:
    print(str(bin(n))[2:])
else:
    tmp = str(bin(abs(n) + 1))[2:]
    answer = ''
    for t in tmp:
        if t == '0':
            answer += '1'
        else:
            answer += '0'
    print(int(answer))

