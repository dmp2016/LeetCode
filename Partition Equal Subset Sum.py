from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        d = sum(nums)
        if d & 1:
            return False
        target = d // 2
        sm = set()

        for a in nums:
            for k in sm.copy():
                sm.add(k + a)
            sm.add(a)
            if target in sm:
                return True
        return False


test = Solution()
print(test.canPartition(nums=[1, 5, 11, 5]))
print(test.canPartition(nums=[1, 2, 3, 5]))
