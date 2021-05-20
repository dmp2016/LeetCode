from typing import List
from collections import Counter


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        h = len(nums) // 2
        r = nums[h]

        res = 0
        for a in nums:
            res += abs(a - r)
        return res

        res = 0
        d = Counter(nums)
        d = sorted([[elem, d[elem]] for elem in d])
        ind1, ind2 = 0, len(d) - 1
        while ind1 < ind2:
            a1 = d[ind1 + 1][0] - d[ind1][0]
            b1 = d[ind1][1]

            a2 = d[ind2][0] - d[ind2 - 1][0]
            b2 = d[ind2][1]

            if a1 * b1 <= a2 * b2:
                res += a1 * b1
                ind1 += 1
                d[ind1][1] += d[ind1 - 1][1]
            else:
                res += a2 * b2
                ind2 -= 1
                d[ind2][1] += d[ind2 + 1][1]
        return res


test = Solution()
# print(test.minMoves2(nums=[1, 2, 3]))
print(test.minMoves2(nums=[1, 10, 2, 9]))
