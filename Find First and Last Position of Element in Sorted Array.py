from typing import List
from bisect import bisect_left, bisect_right


class Solution:
    def searchRange1(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        ind1 = bisect_left(nums, target)
        if ind1 == len(nums) or nums[ind1] != target:
            return [-1, -1]
        ind2 = bisect_right(nums, target)
        return [ind1, ind2 - 1]

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]

        if target < nums[0] or target > nums[-1]:
            return [-1, -1]
        if target == nums[0]:
            ind1 = 0
        else:
            left, right = 0, len(nums) - 1
            while right - left > 1:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid
                else:
                    right = mid
            if nums[right] == target:
                ind1 = right
            else:
                return [-1, -1]
        if target == nums[-1]:
            ind2 = len(nums) - 1
        else:
            left, right = 0, len(nums) - 1
            while right - left > 1:
                mid = (left + right) // 2
                if nums[mid] > target:
                    right = mid
                else:
                    left = mid
            ind2 = left
        return [ind1, ind2]


test = Solution()
print(test.searchRange(nums=[5, 7, 7, 8, 8, 10], target=5))
print(test.searchRange(nums=[5, 7, 7, 8, 8, 10], target=10))
print(test.searchRange(nums=[5, 7, 7, 8, 8, 10], target=7))
print(test.searchRange(nums=[5, 7, 7, 8, 8, 10], target=8))
print(test.searchRange(nums=[5, 7, 7, 8, 8, 10], target=6))
print(test.searchRange(nums=[], target=0))
