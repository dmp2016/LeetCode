from typing import List
from collections import Counter
import math


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        res = math.inf
        for num in range(1, 7):
            cnt_both = 0
            cnt_top = 0
            cnt_bot = 0
            for ind in range(n):
                if tops[ind] == num and bottoms[ind] == num:
                    cnt_both += 1
                elif tops[ind] == num:
                    cnt_top += 1
                elif bottoms[ind] == num:
                    cnt_bot += 1
            if cnt_both + cnt_top + cnt_bot == n:
                res = min(cnt_top, cnt_bot)
        return res if res < math.inf else -1


test = Solution()
print(test.minDominoRotations(tops=[2, 1, 2, 4, 2, 2], bottoms=[5, 2, 6, 2, 3, 2]))
