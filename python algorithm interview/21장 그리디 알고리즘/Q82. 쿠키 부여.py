"""
fixme. https://leetcode.com/problems/assign-cookies/
fixme. Q82. 쿠키 부여
fixme. 아이들에게 1개씩 쿠키를 나눠줘야 한다. 각 아이 child_i 마다 그리드 패거를 갖고 있으며,
fixme. 이는 아이가 만족하는 최소 쿠키의 크기를 말한다. 각 쿠키 cookie_j는 크기 s(j)를 갖고 있으며,
fixme. s(j) >= g(i)이어야 아이가 만족하며 쿠키를 받는다. 최대 몇명의 아이들에게 쿠키를 줄 수 있는지 출력하라.
fixme. 입력 : [1, 2, 3], [1, 1]
fixme. 출력 : 1
fixme. 설명
fixme. 두번 때 아이부터는 크기 2 이사의 쿠키가 필요하지만, 갖고 있는 최대 크기는 1이기 때문에 1명의 아이에게만 줄 수 있다.

fixme. 입력 : [1, 2], [1, 2, 3]
fixme. 출력 : 2
fixme. 설명
fixme. 충분한 쿠키를 갖고 있고, 2명 모두에게 쿠키를 줄 수 있다.
"""

from typing import List
import bisect


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        child_i = cookie_j = 0
        # 만족하지 못할 때까지 그리디 진행
        while child_i < len(g) and cookie_j < len(s):
            if s[cookie_j] >= g[child_i]:
                child_i += 1
            cookie_j += 1

        return child_i

    def findContentChildrenBisect(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        result = 0
        for i in s:
            # 이진 검색으로 더 큰 인덱스 탐색
            index = bisect.bisect_right(g, i)
            if index > result:
                result += 1

        return result
