from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        cur_r = nums[0]
        ind1 = None
        ind2 = None
        for ind in range(1, len(nums)):
            if nums[ind] < cur_r:
                if ind1 is None:
                    ind1 = ind
                else:
                    if nums[ind] < nums[ind1]:
                        ind1 = ind
                ind2 = ind
            cur_r = max(cur_r, nums[ind])
        if ind1 is None:
            return 0
        ind0 = 0
        for ind in range(len(nums)):
            if nums[ind] > nums[ind1]:
                ind0 = ind
                break
        return ind2 - ind0 + 1
            
test = Solution()
print(test.findUnsortedSubarray(nums = [2,6,4,8,10,9,15]))
print(test.findUnsortedSubarray(nums = [1,2,3,4]))
print(test.findUnsortedSubarray(nums = [1]))
