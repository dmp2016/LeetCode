from typing import List
from collections import defaultdict


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        prev_set = set()
        pairs = set()
        res = 0
        for a in nums:
            if a - k in prev_set:
                pairs.add((a - k, a))
                pairs.add((a, a - k))
            if k + a in prev_set:
                pairs.add((k + a, a))
                pairs.add((a, k + a))
            prev_set.add(a)
        if k == 0:
            return len(pairs)
        else:
            return len(pairs) // 2


test = Solution()
print(test.findPairs(nums=[3, 1, 4, 1, 5], k=2))
print(test.findPairs(nums=[1, 2, 3, 4, 5], k=1))
print(test.findPairs(nums=[1, 3, 1, 5, 4], k=0))
print(test.findPairs(nums=[1, 2, 4, 4, 3, 3, 0, 9, 2, 3], k=3))
