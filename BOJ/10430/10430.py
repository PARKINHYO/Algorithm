a, b, c = input().split(" ", 2)
print((int(a)+int(b)) % int(c))
print((int(a) % int(c) + int(b) % int(c)) % int(c))
print(int(a)*int(b) % int(c))
print((int(a) % int(c)*int(b)%int(c)) % int(c))