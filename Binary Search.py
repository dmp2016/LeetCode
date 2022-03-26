from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target < nums[0] or target > nums[-1]:
            return -1
        l, r = 0, len(nums) - 1
        while r > l:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        return r if r < len(nums) and target == nums[r] else -1


test = Solution()
print(test.search(nums=[-1, 0, 3, 5, 9, 12], target=9))
print(test.search(nums=[-1, 0, 3, 5, 9, 12], target=2))
print(test.search(nums=[0, 2], target=2))
print(test.search(nums=[0, 2], target=0))
print(test.search(nums=[1], target=1))
