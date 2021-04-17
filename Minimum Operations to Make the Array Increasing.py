from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        for ind in range(1, len(nums)):
            delta = nums[ind - 1] - nums[ind]
            if delta >= 0:
                res += delta + 1
                nums[ind] += delta + 1
        return res


test = Solution()
print(test.minOperations(nums=[1, 1, 1]))
print(test.minOperations(nums=[1, 5, 2, 4, 1]))
print(test.minOperations(nums=[8]))
