from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = list()
        for n in nums:
            heapq.heappush(heap, -n)


        for _ in range(1, k):
            print(heapq.heappop(heap))

        return -heapq.heappop(heap)


print(Solution().findKthLargest([3,2,3,1,2,4,5,5,6], 4))
