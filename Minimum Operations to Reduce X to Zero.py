from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        if x == 0:
            return 0
        cum_rights = {0: len(nums)}
        cum_right = 0
        for ind in range(len(nums)):
            cum_right += nums[len(nums) - ind - 1]
            cum_rights[cum_right] = len(nums) - ind - 1
        cum_left = 0
        res = len(nums) + 1
        if x in cum_rights:
            res = min(res, len(nums) - cum_rights[x])
        for ind in range(len(nums)):
            cum_left += nums[ind]
            ind_r = cum_rights.get(x - cum_left)
            if ind_r is not None and ind_r > ind:
                res = min(res, len(nums) - ind_r + ind + 1)
        return res if res <= len(nums) else -1


test = Solution()
# print(test.minOperations(nums=[1, 1, 4, 2, 3], x=5))
# print(test.minOperations(nums=[5, 6, 7, 8, 9], x=4))
# print(test.minOperations(nums=[3, 2, 20, 1, 1, 3], x=10))
# print(test.minOperations(nums=[30, 2, 20, 1, 1, 3], x=30))
print(test.minOperations(nums=[8828, 9581, 49, 9818, 9974, 9869, 9991, 10000, 10000, 10000, 9999, 9993, 9904, 8819, 1231, 6309], x=134365))
