S = [i for i in input()]
ex = [int(-1)]
alphabet = ex*26
for i in range(len(S)):
    if S[i] == 'a':
        alphabet[0] = S.index('a')
    elif S[i] == 'b':
        alphabet[1] = S.index('b')
    elif S[i] == 'c':
        alphabet[2] = S.index('c')
    elif S[i] == 'd':
        alphabet[3] = S.index('d')
    elif S[i] == 'e':
        alphabet[4] = S.index('e')
    elif S[i] == 'f':
        alphabet[5] = S.index('f')
    elif S[i] == 'g':
        alphabet[6] = S.index('g')
    elif S[i] == 'h':
        alphabet[7] = S.index('h')
    elif S[i] == 'i':
        alphabet[8] = S.index('i')
    elif S[i] == 'j':
        alphabet[9] = S.index('j')
    elif S[i] == 'k':
        alphabet[10] = S.index('k')
    elif S[i] == 'l':
        alphabet[11] = S.index('l')
    elif S[i] == 'm':
        alphabet[12] = S.index('m')
    elif S[i] == 'n':
        alphabet[13] = S.index('n')
    elif S[i] == 'o':
        alphabet[14] = S.index('o')
    elif S[i] == 'p':
        alphabet[15] = S.index('p')
    elif S[i] == 'q':
        alphabet[16] = S.index('q')
    elif S[i] == 'r':
        alphabet[17] = S.index('r')
    elif S[i] == 's':
        alphabet[18] = S.index('s')
    elif S[i] == 't':
        alphabet[19] = S.index('t')
    elif S[i] == 'u':
        alphabet[20] = S.index('u')
    elif S[i] == 'v':
        alphabet[21] = S.index('v')
    elif S[i] == 'w':
        alphabet[22] = S.index('w')
    elif S[i] == 'x':
        alphabet[23] = S.index('x')
    elif S[i] == 'y':
        alphabet[24] = S.index('y')
    else:
        alphabet[25] = S.index('z')

for i in alphabet:
    print(i, end=' ')