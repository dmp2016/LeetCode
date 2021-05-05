from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_dist = 0
        for ind in range(len(nums)):
            if ind <= max_dist:
                max_dist = max(max_dist, ind + nums[ind])
        return max_dist >= len(nums) - 1


test = Solution()
print(test.canJump(nums=[2, 3, 1, 1, 4]))
print(test.canJump(nums=[3, 2, 1, 0, 4]))
