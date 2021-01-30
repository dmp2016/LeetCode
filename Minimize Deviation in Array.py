from typing import List
from sortedcontainers import SortedList


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        maxv = nums.copy()
        for ind in range(len(maxv)):
            if maxv[ind] & 1:
                maxv[ind] <<= 1
        for ind in range(len(nums)):
            while not nums[ind] & 1:
                nums[ind] >>= 1
        ind_nums = SortedList([(nums[ind], ind) for ind in range(len(nums))])
        res = ind_nums[-1][0] - ind_nums[0][0]
        while ind_nums[0][0] < maxv[ind_nums[0][1]]:
            a, b = ind_nums[0]
            del ind_nums[0]
            ind_nums.add((2 * a, b))
            if res > ind_nums[-1][0] - ind_nums[0][0]:
                res = ind_nums[-1][0] - ind_nums[0][0]
        return res


test = Solution()
print(test.minimumDeviation(nums=[1, 2, 3, 4]))
print(test.minimumDeviation(nums=[4, 1, 5, 20, 3]))
