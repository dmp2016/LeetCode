from typing import List
from bisect import bisect_left, bisect_right


class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        nums0 = [nums[ind] for ind in range(0, len(nums) - 3) if nums[ind] != nums[ind + 3]]
        nums0 += nums[-3:]
        nums = nums0
        ind_a_min = bisect_left(nums, - nums[-1] - nums[-2], 0, len(nums) - 3)
        nums3 = [nums[ind] + nums[ind + 1] + nums[ind + 2] for ind in range(0, len(nums) - 2)]
        ind_a_max = bisect_right(nums3, 0, 0, len(nums3))
        res = set()
        for ind1 in range(ind_a_min, ind_a_max):
            a = nums[ind1]
            ind_b_min = bisect_left(nums, -a - nums[-1], ind1 + 1, len(nums) - 2)
            nums2 = [nums[ind] + nums[ind + 1] for ind in range(0, len(nums) - 1)]
            ind_b_max = bisect_right(nums2, -a, ind1 + 1, len(nums2))
            for ind2 in range(ind_b_min, ind_b_max):
                b = nums[ind2]
                c_ind = bisect_left(nums, - a - b, ind2 + 1)
                if c_ind < len(nums) and nums[c_ind] == -a - b:
                    res.add((a, b, nums[c_ind]))
        res = set(res)
        return list(res)

test = Solution()
A = [-1,0,1,2,-1,-4]
res = test.threeSum(A)
print(res)
