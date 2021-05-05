from typing import List
import math


class Solution:
    def jump(self, nums: List[int]) -> int:
        dist = [math.inf] * len(nums)
        dist[0] = 0
        for ind1 in range(len(nums)):
            for ind2 in range(ind1 + 1, min(len(nums), ind1 + nums[ind1] + 1)):
                dist[ind2] = min(dist[ind1] + 1, dist[ind2])
        return dist[-1]


test = Solution()
print(test.jump(nums=[2, 3, 1, 1, 4]))
print(test.jump(nums=[2, 3, 0, 1, 4]))
