from typing import List
import numpy as np
from bisect import bisect_left


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        cs = np.cumsum(nums)
        s0 = 0
        res = 0
        for ind1 in range(len(cs)):
            ind2 = bisect_left(cs, s + s0, ind1)
            if ind2 < len(cs) and (ind2 - ind1 + 1 < res or res == 0):
                res = ind2 - ind1 + 1
                self.ind1 = ind1
                self.ind2 = ind2
            s0 = cs[ind1]
        return res


test = Solution()
print(test.minSubArrayLen(7, [2, 3, 1, 2, 4, 1]))
print(test.minSubArrayLen(7, []))
