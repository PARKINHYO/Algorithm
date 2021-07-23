import sys
input = sys.stdin.readline


class Solution: 
    def ACM_hotel(self, H: int, W: int, N: int):
        floor = str(N%H)
        door = str((N//H)+1)
        if floor == '0':
            floor = str(H)
            door = str((N//H))
        if len(door) == 1:
            door = '0' + door
        return floor + door
            


for _ in range(int(input())):
    H, W, N = map(int, input().split())
    print(Solution().ACM_hotel(H,W,N))