import collections

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        freqs = collections.defaultdict(int)
        count = 0

        for char in S:
            freqs[char] += 1

        for char in J:
            count += freqs[char]

        return count

