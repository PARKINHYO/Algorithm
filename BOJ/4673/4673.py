setSelf = set(i for i in range(1, 10001))
setF = set()
for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    setF.add(i)
setSelf = sorted(setSelf - setF)
for i in setSelf:
    print(i)