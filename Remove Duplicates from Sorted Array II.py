from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ind1, ind2 = 1, 1
        prev = nums[0]
        prev_cnt = 1
        while ind2 < len(nums):
            if prev == nums[ind2]:
                prev_cnt += 1
            else:
                prev_cnt = 1
                prev = nums[ind2]
                        
            if prev_cnt <= 2:
                nums[ind1] = nums[ind2]
                ind1 += 1
            ind2 += 1
        return ind1


test = Solution()
nums=[1, 1, 1, 1, 1, 2, 2, 3]
print(test.removeDuplicates(nums))
print(nums)
nums=[0, 0, 1, 1, 1, 1, 2, 3, 3]
print(test.removeDuplicates(nums))
print(nums)
