from typing import List


class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        mask = 1
        for _ in range(maximumBit - 1):
            mask <<= 1
            mask |= 1
        cx = nums[0]
        for ind in range(1, len(nums)):
            cx ^= nums[ind]
        res = []
        for ind in range(len(nums) - 1, -1, -1):
            a = cx & mask
            res.append((~a) & mask)
            cx ^= nums[ind]
        return res


test = Solution()
print(test.getMaximumXor(nums=[0, 1, 1, 3], maximumBit=2))
print(test.getMaximumXor(nums=[2, 3, 4, 7], maximumBit=3))
print(test.getMaximumXor(nums=[0, 1, 2, 2, 5, 7], maximumBit=3))
