from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = 2 ** len(nums)
        for k in range(n):
            a = []
            t = k
            for i in range(len(nums)):
                if t & 1:
                    a.append(nums[i])
                t >>= 1
            res.append(a)
        return res


test = Solution()
print(test.subsets([1, 2, 3]))
