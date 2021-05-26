from typing import List


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        h = len(nums) // 2
        r = nums[h]

        res = 0
        for a in nums:
            res += abs(a - r)
        return res


test = Solution()
print(test.minMoves2(nums=[1, 2, 3]))
print(test.minMoves2(nums=[1, 10, 2, 9]))
