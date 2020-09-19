from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ind1, ind2 = None, None
        for i in range(len(nums)):
            if nums[i] == 2:
                if ind2 is None:
                    ind2 = i
                continue
            if nums[i] == 1:
                if ind2 is not None:
                    nums[ind2] = 1
                    if ind1 is None:
                        ind1 = ind2
                    nums[i] = 2
                    ind2 += 1
                elif ind1 is None:
                    ind1 = i
                continue
            if nums[i] == 0:
                if ind1 is not None:
                    nums[ind1] = 0
                    ind1 += 1
                    if ind2 is not None:
                        nums[ind2] = 1
                        ind2 += 1
                        nums[i] = 2
                    else:
                        nums[i] = 1
                elif ind2 is not None:
                    nums[ind2] = 0
                    ind2 += 1
                    nums[i] = 2


test = Solution()
nums = [2, 0, 2, 1, 1, 0]
test.sortColors(nums)
print(nums)
nums = [2, 0, 1]
test.sortColors(nums)
print(nums)
nums = [0]
test.sortColors(nums)
print(nums)
nums = [1, 0, 1, 0, 1, 1]
test.sortColors(nums)
print(nums)
nums = [2, 0, 2, 0, 2, 2]
test.sortColors(nums)
print(nums)
nums = [2, 1, 2, 1, 2, 2]
test.sortColors(nums)
print(nums)
