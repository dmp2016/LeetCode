from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        rem = sum(nums) % p
        if rem == 0:
            return 0
        n_rems = {0: -1}
        sm = 0
        res = len(nums)
        for ind in range(len(nums)):
            sm += nums[ind]
            sm %= p
            if (sm - rem) % p in n_rems and ind - n_rems[(sm - rem) % p] < res:
                res = ind - n_rems[(sm - rem) % p]
            n_rems[sm] = ind
        return res if res < len(nums) else -1


test = Solution()
print(test.minSubarray(nums = [3,1,4,2], p = 6))
print(test.minSubarray(nums = [6,3,5,2], p = 9))
print(test.minSubarray(nums = [1,2,3], p = 3))
print(test.minSubarray(nums = [1,2,3], p = 7))
