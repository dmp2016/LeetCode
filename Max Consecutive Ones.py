from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        cur = 0
        for a in nums:
            if a != 1:
                res = max(cur, res)
                cur = 0
            else:
                cur += 1
        res = max(cur, res)
        return res


test = Solution()
print(test.findMaxConsecutiveOnes(nums=[1, 1, 0, 1, 1, 1]))
print(test.findMaxConsecutiveOnes(nums=[1, 0, 1, 1, 0, 1]))
print(test.findMaxConsecutiveOnes(nums=[1]))
print(test.findMaxConsecutiveOnes(nums=[0]))
print(test.findMaxConsecutiveOnes(nums=[]))
