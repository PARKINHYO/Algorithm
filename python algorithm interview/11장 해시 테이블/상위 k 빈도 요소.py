from typing import List
import collections
import heapq

# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         freqs = collections.Counter(nums)
#         freqs_heap = []
#
#         for f in freqs:
#             heapq.heappush(freqs_heap, (-freqs[f], f))
#
#         topk = list()
#         for _ in range(k):
#             topk.append(heapq.heappop(freqs_heap)[1])
#
#         return topk

class Solution:
    def topKFrequent(self, nums, k):
        return list(zip(*collections.Counter(nums).most_common(k)))[0]

    