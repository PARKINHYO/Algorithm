"""
fixme. https://leetcode.com/problems/utf-8-validation
fixme. Q73. UTF-8 검증
fixme. 입력값이 UTF-8 문자열이 맞는지 검증하라.
fixme. 예제1 : data = [197, 130, 1], 이 값은 11000101, 10000010 00000001로
fixme. 표현되며, 2바이트 문자 다음에 오는 1바이트 문자로, 모두 2개며 정상이다.
fixme. 예제2 : data = [235, 140, 4], 이 값은 11101011, 10001100, 00000100로 표현되며,
fixme. 첫 바이트의 첫 3비트가 모두 1이고 4번째 비트가 0이므로 3바이트 문자임을 뜻한다.
fixme. 다음 바이트도 10으로 시작하여 정상이지만, 그다음 바이트는 10으로 시작하지 않으므로 비정상이다.
"""

from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        # 문자 바이트 만큼 10으로 시작 판별
        def check(size):
            for i in range(start + 1, start + size + 1):
                if i >= len(data) or (data[i] >> 6) != 0b10:
                    return False
            return True

        start = 0
        while start < len(data):
            # 첫 바이트 기준 총 문자 바이트 판별
            first = data[start]
            if (first >> 3) == 0b11110 and check(3):
                start += 4
            elif (first >> 4) == 0b1110 and check(2):
                start += 3
            elif(first >> 5) == 0b110 and check(1):
                start += 2
            elif (first >>7) == 0:
                start += 1
            else:
                return False
        return True