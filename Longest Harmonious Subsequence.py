from typing import List
from collections import Counter


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        return max([cnt[n] + cnt[n + 1] for n in cnt.keys() if n + 1 in cnt.keys()], default=0)


test = Solution()
print(test.findLHS([1,3,2,2,5,2,3,7]))
print(test.findLHS([1,1]))
