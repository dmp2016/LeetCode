from typing import List
from bisect import bisect_left, bisect_right
import math


class Solution:
    def threeSumClosest_1(self, nums: List[int], target: int) -> int:
        nums.sort()
        delta = math.inf
        res = math.inf
        for ind1 in range(len(nums) - 2):
            target1 = target - nums[ind1]
            for ind2 in range(ind1 + 1, len(nums) - 1):
                target2 = target1 - nums[ind2]
                left_lim = max(bisect_left(nums, target2, lo = ind2 + 1) - 1, ind2 + 1)
                right_lim = min(bisect_right(nums, target2, lo = ind2 + 1) + 1, len(nums))
                for ind3 in range(left_lim, right_lim):
                    if delta > abs(target2 - nums[ind3]):
                        delta = abs(target2 - nums[ind3])
                        res = nums[ind1] + nums[ind2] + nums[ind3]
        return res

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        delta = math.inf
        res = math.inf
        for ind1 in range(len(nums) - 2):
            ind2, ind3 = ind1 + 1, len(nums) - 1
            while ind2 < ind3:
                sm = nums[ind1] + nums[ind2] + nums[ind3]
                new_delta = abs(target - sm)
                if delta > abs(new_delta):
                    delta = new_delta
                    res = sm
                if sm > target:
                    ind3 -= 1
                elif sm < target:
                    ind2 += 1
                else:
                    break
            sm = nums[ind1] + nums[ind2] + nums[ind3]
        return res


test = Solution()
# print(test.threeSumClosest(nums=[-1, 2, 1, -4], target=1))
# print(test.threeSumClosest(nums=[777, -251, -381, -946, -491, -58, 343, 888, -227, -704, 460, 64, -144, 706, -891, 806, -577, 606, 684, -612, 502, -433, -304, -375, -128, -82, 77, 256, -541, -34, -502, 304, 89, 174, -617, -39, -558, 897, 708, 695, -250, 984, 986, -106, 110, 126, 383, 421, -8, -335, -776, 926, -785, -656, -419, -433, -182, -986, -964, 52, -357, -514, -238, 329, 87, 25, 443, -104, 78, -696, -178, 419, 790, -17, 752, 151, 433, 439, -120, -953, 750, 845, 608, -405, -759, 939, 574, -691, 572, -862, -317, -275, 226, 821, 528, 10, -472, -284, -382, 524], target=18))
# print(test.threeSumClosest(nums=[0,0,0], target = 1))
print(test.threeSumClosest(nums=[1, 2, 5, 10, 11], target=12))
