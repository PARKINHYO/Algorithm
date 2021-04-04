class Solution:
    def josephus(self, N: int, K: int):
        persons = [x for x in range(1, N+1)]
        idx = 0
        answer = []
        for _ in range(N):
            idx += (K-1)
            if idx >= len(persons):
                idx = idx % len(persons)
            answer.append(str(persons.pop(idx)))
        print("<", ", ".join(answer), ">", sep="")


N, K = map(int, input().split())
Solution().josephus(N, K)

