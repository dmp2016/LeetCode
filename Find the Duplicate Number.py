from cgi import test
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums) - 1
        left, right = 1, n
        if sum(1 for a in nums if a == 1) > 1:
            return 1
        while left + 1 < right:
            m = (left + right) // 2
            k = sum(1 for a in nums if a <= m)
            if k > m:
                right = m
            else:
                left = m
        return right


test = Solution()
print(test.findDuplicate(nums=[1, 3, 4, 2, 2]))
print(test.findDuplicate(nums=[3, 1, 3, 4, 2]))
