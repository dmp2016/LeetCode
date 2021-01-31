from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        max_ind = len(nums) - 1
        for cur_ind in range(len(nums) - 2, -1, -1):
            if nums[cur_ind] < nums[max_ind]:
                break
            else:
                max_ind = cur_ind
        else:
            for ind in range(len(nums) // 2):
                nums[ind], nums[len(nums) - ind - 1] = nums[len(nums) - ind - 1], nums[ind]
            return
        for ind in range(cur_ind, len(nums)):
            if nums[cur_ind] < nums[ind] < nums[max_ind]:
                max_ind = ind
        nums[max_ind], nums[cur_ind] = nums[cur_ind], nums[max_ind]
        b = True
        while b:
            b = False
            for ind in range(cur_ind + 1, len(nums) - 1):
                if nums[ind] > nums[ind + 1]:
                    b = True
                    nums[ind], nums[ind + 1] = nums[ind + 1], nums[ind]


test = Solution()
nums = [1, 2, 3]
test.nextPermutation(nums)
print(nums)
nums = [3, 2, 1]
test.nextPermutation(nums)
print(nums)
nums = [1, 1, 5]
test.nextPermutation(nums)
print(nums)
nums = [1]
test.nextPermutation(nums)
print(nums)
nums = [1, 3, 2]
test.nextPermutation(nums)
print(nums)
