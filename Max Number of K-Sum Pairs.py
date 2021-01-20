from typing import List
from collections import Counter, defaultdict
from bisect import bisect_left, bisect


class Solution:
    def maxOperations1(self, nums: List[int], k: int) -> int:
        res = 0
        cnt = Counter(nums)
        res = sum([min(cnt[k - n], cnt[n]) for n in cnt if n < (k + 1) // 2])
        if k % 2 == 0:
            res += cnt[k // 2] // 2
        return res

    def maxOperations2(self, nums: List[int], k: int) -> int:
        res = 0
        nums.sort()
        ind1, ind2 = 0, len(nums) - 1
        while ind1 < ind2:
            if nums[ind1] + nums[ind2] > k:
                ind2 -= 1
            elif nums[ind1] + nums[ind2] < k:
                ind1 += 1
            else:
                res += 1
                ind2 -= 1
                ind1 += 1
        return res

    def maxOperations(self, nums: List[int], k: int) -> int:
        res = 0
        cnt = defaultdict(int)
        for n in nums:
            if cnt[k - n] > 0:
                res += 1
                cnt[k - n] -= 1
            else:
                cnt[n] += 1
        return res

test = Solution()
print(test.maxOperations(nums=[1, 2, 3, 4], k=5))
print(test.maxOperations(nums=[3, 1, 3, 4, 3], k=6))
print(test.maxOperations(nums=[2,5,4,4,1,3,4,4,1,4,4,1,2,1,2,2,3,2,4,2], k=3))
