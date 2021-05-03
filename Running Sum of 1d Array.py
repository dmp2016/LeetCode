from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        cur = 0
        for a in nums:
            cur += a
            res.append(cur)
        return res

