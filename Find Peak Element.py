from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right + 1) // 2
            if mid == 0 or nums[mid - 1] < nums[mid]:
                left = mid
            else:
                right = mid - 1
        return left


test = Solution()
print(test.findPeakElement([1,2,3,1]))
print(test.findPeakElement([1]))
print(test.findPeakElement([1,2,1,3,5,6,4]))
