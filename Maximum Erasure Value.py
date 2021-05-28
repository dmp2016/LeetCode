from typing import List
from collections import defaultdict


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        ind1 = 0
        ind2 = 0
        cur_sum = 0
        res = 0
        cur_set = defaultdict(int)
        while ind2 < len(nums):
            if nums[ind2] not in cur_set:
                cur_set[nums[ind2]] += 1
                cur_sum += nums[ind2]
                res = max(res, cur_sum)
                ind2 += 1
            else:
                cur_set[nums[ind1]] -= 1
                if not cur_set[nums[ind1]]:
                    del cur_set[nums[ind1]]
                cur_sum -= nums[ind1]
                ind1 += 1
        return res        
            
test = Solution()
print(test.maximumUniqueSubarray(nums=[4, 2, 4, 5, 6]))
print(test.maximumUniqueSubarray(nums=[5, 2, 1, 2, 5, 2, 1, 2, 5]))
