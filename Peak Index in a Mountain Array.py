from typing import List


class Solution:
    def peakIndexInMountainArray(self, nums: List[int]) -> int:
        left, right = -1, len(nums)
        while left + 1 < right:
            mid = (left + right) // 2
            if mid < len(nums) - 1 and nums[mid] < nums[mid + 1]:
                left = mid
            elif mid > 0 and nums[mid] < nums[mid - 1]:
                right = mid
            else:
                return mid
        return left + 1

test = Solution()
print(test.peakIndexInMountainArray([24,69,100,99,79,78,67,36,26,19]))
