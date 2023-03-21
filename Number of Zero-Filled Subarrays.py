from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = 0
        k = 0
        while k < len(nums):
            n = 0
            while k < len(nums) and nums[k] == 0:
                k += 1
                n += 1
            res += n * (n + 1) // 2
            k += 1
        return res


test = Solution()
print(test.zeroFilledSubarray(nums=[1, 3, 0, 0, 2, 0, 0, 4]))
print(test.zeroFilledSubarray(nums=[0, 0, 0, 2, 0, 0]))
print(test.zeroFilledSubarray(nums=[2, 10, 2019]))
