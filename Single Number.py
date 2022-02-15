from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for a in nums:
            res ^= a
        return res


test = Solution()
print(test.singleNumber(nums=[-2, -2, 1]))
print(test.singleNumber(nums=[4, 1, 2, 1, 2]))
print(test.singleNumber(nums=[-1]))
print(test.singleNumber(nums=[-2, -2, 1000]))
