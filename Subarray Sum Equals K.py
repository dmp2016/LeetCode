from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = {0: 1}
        cnt = 0
        sm = 0
        for n in nums:
            sm += n
            cnt += sums.get(sm - k, 0)
            sums[sm] = sums.get(sm, 0) + 1
        return cnt
        

test = Solution()
print(test.subarraySum(nums = [1,1,1], k = 2))
print(test.subarraySum(nums = [1,2,3], k = 3))
