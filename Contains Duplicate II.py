from typing import List
from collections import defaultdict


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        inds = defaultdict(list)
        for ind in range(len(nums)):
            inds[nums[ind]].append(ind)
        for n in inds.keys():
            for i in range(1, len(inds[n])):
                if inds[n][i] - inds[n][i - 1] <= k:
                    return True
        return False


test = Solution()
print(test.containsNearbyDuplicate(nums = [1,2,3,1], k = 3))
print(test.containsNearbyDuplicate(nums = [1,0,1,1], k = 1))
print(test.containsNearbyDuplicate(nums = [1,2,3,1,2,3], k = 2))
