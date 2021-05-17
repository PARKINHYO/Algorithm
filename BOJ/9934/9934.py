import sys




K = int(sys.stdin.readline())
buildings = list(map(int, sys.stdin.readline().split()))

bucket = []
bucket.append(buildings)
for i in range(K):
    answer = []
    tmp = []
    while True:
        if not bucket:
            break
        
        cur = bucket.pop(0)
        answer.append(cur[len(cur)//2])
        tmp.append(cur[0:len(cur)//2])
        tmp.append(cur[len(cur)//2+1:])

    bucket = tmp[:]
            
    
    
    print(*answer)