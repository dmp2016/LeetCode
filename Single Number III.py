from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_all = 0
        for item in nums:
            xor_all ^= 0xFFFFFFFF & item
        pt = xor_all & (-xor_all)
        a = 0
        for item in nums:
            if item & pt:
                a ^= 0xFFFFFFFF & item
        b = xor_all ^ a
        if a > 0x7FFFFFFF:
            a = -((a ^ 0xFFFFFFFF) + 1)
        if b > 0x7FFFFFFF:
            b = -((b ^ 0xFFFFFFFF) + 1)
        return (a, b)


test = Solution()
print(test.singleNumber(nums=[1, 2, 1, 3, 2, 5]))
print(test.singleNumber(nums=[-1, 0]))
print(test.singleNumber(nums=[1,1,0,-2147483648]))
