from typing import List
# import numpy as np
from bisect import bisect_left


class Solution:
    # shortest
    # def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:        
    #     nums = np.array(nums)
    #     return [np.sum(nums < a) for a in nums]

    # Fastest
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:        
        nums0 = nums.copy()
        nums0.sort()        
        return [bisect_left(nums0, a) for a in nums]


test = Solution()
nums = [6,5,4,8]
print(test.smallerNumbersThanCurrent(nums))
