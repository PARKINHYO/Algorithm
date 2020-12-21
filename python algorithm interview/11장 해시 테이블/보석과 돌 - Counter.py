import collections

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        freqs = collections.Counter(S)
        count = 0

        for char in J:
            count += freqs[char]

        return count