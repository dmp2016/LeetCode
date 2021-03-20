from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        shift = 0
        for ind in range(len(nums)):
            if nums[ind] == 0:
                shift += 1
            else:
                nums[ind - shift] = nums[ind]
        for ind in range(len(nums) - shift, len(nums)):
            nums[ind] = 0


test = Solution()
nums = [8, 0, 1, 0, 3, 12, 0]
test.moveZeroes(nums)
print(nums)
nums = [0]
print(test.moveZeroes(nums))
print(nums)
