from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        cum_sum = {0: -1}
        sm = 0
        res = 0
        for ind in range(len(nums)):
            sm += 2 * nums[ind] - 1
            if not sm in cum_sum:
                cum_sum[sm] = ind
            else:
                res = max(res, ind - cum_sum[sm])
        return res

test = Solution()
print(test.findMaxLength([0,1]))
print(test.findMaxLength([0,1,0]))
