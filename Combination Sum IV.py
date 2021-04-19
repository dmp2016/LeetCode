from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        d = [0] * (target + 1)
        d[0] = 1

        for k in range(target + 1):
            for a in nums:
                if k - a >= 0:
                    d[k] += d[k - a]
                else:
                    break
        return d[-1]


test = Solution()
print(test.combinationSum4(nums=[1, 2, 3], target=4))
print(test.combinationSum4(nums=[9], target=3))
