"""
fixme. https://leetcode.com/problems/task-scheduler/
fixme. Q80. 태스크 스케줄러
fixme. A에서 Z로 표현된 테스크가 있다. 각 간격마다 CPU는 한 번의 태스크만 실행할 수 있고,
fixme. n번의 간격 내에는 동일한 테스크를 실행할 수 없다. 더 이상 태스크를 실행할 수 없는 경우 아이들(idle) 상태가 된다.
fixme. 모든 테스크를 실행하기 위한 최소 간격을 출력하라.
fixme. 입력 : tasks = ["A","A","A","B","B","B"], n = 2
fixme. 출력 : 8
fixme. 설명 : A -> B -> idle -> A -> B -> idle -> A -> B
"""

from typing import List
import collections


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        result = 0

        while True:
            sub_count = 0
            print("while")
            # 개수 순 추출
            for tasks, _ in counter.most_common(n+1):
                print(counter)
                sub_count += 1
                result += 1

                counter.subtract(tasks)
                # 0 이하인 아이템을 목록에서 완전히 제거
                counter += collections.Counter()

            if not counter:
                break

            result += n - sub_count + 1
        return result

print(Solution().leastInterval(["A","A","A","B","B","B"], 2))