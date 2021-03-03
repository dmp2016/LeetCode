from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)


test = Solution()
print(test.missingNumber(nums=[3, 0, 1]))
print(test.missingNumber(nums=[0, 1]))
print(test.missingNumber(nums=[9, 6, 4, 2, 3, 5, 7, 0, 1]))
print(test.missingNumber(nums=[0]))
