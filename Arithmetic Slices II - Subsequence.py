from typing import List
from collections import defaultdict


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        cs = [defaultdict(int) for _ in range(len(nums))]
        for ind1 in range(len(nums) - 1, -1, -1):
            for ind2 in range(ind1 + 1, len(nums)):
                cs[ind1][nums[ind2] - nums[ind1]] += cs[ind2][nums[ind2] - nums[ind1]] + 1
        res = 0
        for ind in range(len(cs)):
            res += sum(cs[ind].values())

        return res - (len(nums) * (len(nums) - 1)) // 2


test = Solution()
print(test.numberOfArithmeticSlices(nums=[2, 4, 6, 8, 10]))
print(test.numberOfArithmeticSlices(nums=[7, 7, 7, 7, 7]))
print(test.numberOfArithmeticSlices(nums=[1] * 30))
