from typing import List
from collections import Counter


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        res = 0
        ct = Counter(nums)
        nums = sorted(list(set(nums)))

        cc = dict()
        def do_rec(ind: int) -> int:
            if ind < 0:
                return 0
            if ind in cc:
                return cc[ind]
            a = nums[ind]
            if a - 1 in ct:
                r = max(a * ct[a] + do_rec(ind - 2), do_rec(ind - 1))
            else:
                r = a * ct[a] + do_rec(ind - 1)
            cc[ind] = r
            return r

        return do_rec(len(nums) - 1)


test = Solution()
print(test.deleteAndEarn(nums=[3, 4, 2]))
print(test.deleteAndEarn(nums=[2, 2, 3, 3, 3, 4]))
print(test.deleteAndEarn(nums=[8, 3, 4, 7, 6, 6, 9, 2, 5, 8, 2, 4, 9, 5, 9, 1, 5, 7, 1, 4]))
