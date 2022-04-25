from typing import List
import math


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:

        @lru_cache(maxsize=200000)
        def dyn(ind: int) -> int:
            if ind == len(nums) - 1:
                return nums[ind]
            return nums[ind] + dyn(min(ind + k, len(nums) - 1))

        res = -math.inf
        for i in range(0, k):
            res = max(res, dyn(i))
        return res

    def maxResult1(self, nums: List[int], k: int) -> int:

        def dyn(ind: int) -> int:
            if ind == len(nums) - 1:
                return nums[ind]
            res = -math.inf
            for i in range(ind + 1, min(ind + k + 1, len(nums))):
                res = max(res, dyn(i))
            return nums[ind] + res

        return dyn(0)

test = Solution()
print(test.maxResult(nums=[1, 2], k=2))
print(test.maxResult(nums=[1, -1, -2, 4, -7, 3], k=2))
print(test.maxResult(nums=[10, -5, -2, 4, 0, 3], k=3))
print(test.maxResult(nums=[1, -5, -20, 4, -1, 3, -6, -3], k=2))
