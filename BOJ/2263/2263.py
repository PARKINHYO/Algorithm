import sys
sys.setrecursionlimit(10**6)

n = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))
pos = [0]*(n+1)
for i in range(n):
    pos[in_order[i]] = i

def solution(in_start, in_end, post_start, post_end):
    if in_start > in_end and post_start > post_end:
        return
    
    root = post_order[post_end]
    print(root, end=" ")
    
    left = pos[root] - in_start
    right = in_end - pos[root]
    
    solution(in_start, in_start+left-1, \
        post_start, post_start+left-1 )
    solution(in_end-right+1, in_end, \
        post_end-right, post_end-1)
    
solution(0,n-1,0,n-1)

