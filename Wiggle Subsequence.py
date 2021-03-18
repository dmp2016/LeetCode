from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        res = 1
        p = None
        for ind in range(1, len(nums)):
            if nums[ind] == nums[ind - 1]:
                continue
            if p is None:
                p = nums[ind] > nums[ind - 1]
                res += 1
            elif p and nums[ind] < nums[ind - 1]:
                p = False
                res += 1
            elif not p and nums[ind] > nums[ind - 1]:
                p = True
                res += 1
        return res


test = Solution()
print(test.wiggleMaxLength(nums=[1, 7, 4, 9, 2, 5]))
print(test.wiggleMaxLength(nums=[1, 17, 5, 10, 13, 15, 10, 5, 16, 8]))
print(test.wiggleMaxLength(nums=[1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(test.wiggleMaxLength(nums=[0, 0]))
print(test.wiggleMaxLength(nums=[1]))
