import sys
input = sys.stdin.readline


N, M = map(int, input().split())
not_listen_person = set()
not_see_person = set()
for _ in range(N):
    not_listen_person.add(input().rstrip())
for _ in range(M):
    not_see_person.add(input().rstrip())
answer = list(not_listen_person & not_see_person)
print(len(answer))
answer.sort()
print(*answer)