from sys import stdin
from typing import List


class Solution:
    def meetingRoom(self, schedule: List[List[int]]):
        schedule.sort(key=lambda x: (x[1], x[0]))
        end_time = schedule[0][1]
        count = 1
        for i in range(1, len(schedule)):
            if schedule[i][0] >= end_time:
                count += 1
                end_time = schedule[i][1]

        return count


schedule = []
for _ in range(int(stdin.readline())):
    schedule.append(list(map(int, stdin.readline().split())))

print(Solution().meetingRoom(schedule))
