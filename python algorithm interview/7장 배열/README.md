### 7장 배열

```python
"""
fixme. https://leetcode.com/problems/two-sum/
fixme. 뎃셈하여 타켓을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.

fixme. Input: nums = [2,7,11,15], target = 9
fixme. Output: [0,1]
fixme. Output: BecaInput: nums = [3,2,4], target = 6

fixme. Input: nums = [3,2,4], target = 6
fixme. Output: [1,2]

fixme. Input: nums = [3,3], target = 6
fixme. Output: [0,1]
"""

from typing import List


class Solution:
    def twoSumBruteForce(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSumIn(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            complement = target - n

            if complement in nums[i + 1:]:
                return [nums.index(n), nums[i + 1:].index(complement) + (i + 1)]

    def twoSumDictionary(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        # 키와 값을 바꿔서 딕셔너리로 저장
        for i, num in enumerate(nums):
            nums_map[num] = i

        # 타멧에서 첫 번째 수를 뺀 결과를 키로 조회
        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target - num]:
                return [nums.index(num), nums_map[target - num]]

    def twoSumDictionaryFast(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}

        # 키와 값을 바꿔서 딕셔너리 저장.
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target - num], i]
            nums_map[num] = i
```

<br><br>

```python
"""
fixme. https://leetcode.com/problems/trapping-rain-water/
fixme. Q08. 빗물 트래핑
fixme. 높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 계산하라.

fixme. Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
fixme. Output: 6
fixme. Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
fixme. In this case, 6 units of rain water (blue section) are being trapped.

fixme. Input: height = [4,2,0,3,2,5]
fixme. Output: 9
"""

from typing import List


class Solution:
    def trapTwoPointer(self, height: List[int]) -> int:
        if not height:
            return 0

        volume = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while left < right:
            left_max, right_max = max(left_max, height[left]), max(right_max, height[right])

            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1

        return volume

    def trapStack(self, height: List[int]) -> int:
        stack = []
        volume = 0

        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                print(i)
                top = stack.pop()

                if not len(stack):
                    break

                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]
                volume += distance * waters

            stack.append(i)
        print(stack)
        return volume


Solution().trapStack([0,1,0,2,1,0,1,3,2,1,2,1])
```

<br><br>

```python
"""
fixme. https://leetcode.com/problems/3sum/
fixme. 배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력하라 .

fixme. Input: nums = [-1,0,1,2,-1,-4]
fixme. Output: [[-1,-1,2],[-1,0,1]]
"""

from typing import List


class Solution():
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()

        for i in range(len(nums) - 2):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    results.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

        return results
```

<br><br>

```python
"""
fixme. https://leetcode.com/problems/array-partition-i/
fixme. Q10. 배열 파티션Ⅰ
fixme. n개의 페어를 이용한 min(a, b)의 합으로 만들 수 있는 가장 큰 수를 출력하라 .
fixme. Input: nums = [1,4,3,2]
fixme. Output: 4
fixme. Explanation: All possible pairings (ignoring the ordering of elements) are:
fixme. 1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
fixme. 2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
fixme. 3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
fixme. So the maximum possible sum is 4.
"""

from typing import List

class Solution:
    def arrayPairSum1(self, nums: List[int]) -> int:
        sum = 0
        pair = []
        nums.sort()

        for n in nums:
            pair.append(n)
            if len(pair) == 2:
                sum += min(pair)
                pair = []

        return sum

    def arrayPairSum2(self, nums: List[int]) -> int:
        sum = 0
        nums.sort()

        for i, n in enumerate(nums):
            if i % 2 == 0:
                sum += n

        return sum


    def arrayPairSum3(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])
```

<br><br>

```python
"""
fixme. https://leetcode.com/problems/product-of-array-except-self/
fixme. Q11. 자신을 제외한 배열의 곱
fixme. 배열을 입력받아 output[i]가 자신을 제외한 나머지 모든 요소의 곱셉 결과가 되도록 출력하라.
fixme. Input:  [1,2,3,4]
fixme. Output: [24,12,8,6]
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        p = 1

        for i in range(0, len(nums)):
            out.append(p)
            p = p * nums[i]

        p = 1

        for i in range(len(nums) - 1, -1, -1):
            out[i] = out[i] * p
            p = p * nums[i]

        return out
```

<br><br>

```python
"""
fixme. https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
fixme. Q12. 주식을 사고팔기 가장 좋은 시점
fixme. 한 번의 거래로 낼 수 있는 최대 이익을 산출하라.
fixme. Input: [7,1,5,3,6,4]
fixme. Output: 7
fixme. Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
 Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

fixme. Input: [1,2,3,4,5]
 Output: 4
 Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.

fixme. Input: [7,6,4,3,1]
 Output: 0
 Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""

from typing import List
import sys


class Solution():
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = sys.maxsize

        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)

        return profit
```