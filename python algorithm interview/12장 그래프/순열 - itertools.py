import itertools
from typing import List


class Solution:
    def permute(self, nums: List[int]):
        return list(map(list,itertools.permutations(nums)))
