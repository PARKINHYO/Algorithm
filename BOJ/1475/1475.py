import sys, collections
input = sys.stdin.readline


class Solution:
    def room_number(self, numbers: str):
        plastics = collections.defaultdict(int)
        for number in numbers:
            if number == '6' or number == '9':
                if plastics['6'] == plastics['9']:
                    plastics[number] += 1
                elif plastics['6'] < plastics['9']:
                    plastics['6'] += 1
                else:
                    plastics['9'] += 1
            else:
                plastics[number] += 1
        return collections.Counter(plastics).most_common()[0][1]


print(Solution().room_number(input().rstrip()))