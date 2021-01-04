from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        A = [0] * len(nums)
        for n in nums:
            A[n - 1] += 1
        return [A.index(2) + 1, A.index(0) + 1]

test = Solution()
print(test.findErrorNums(nums = [1,2,2,4]))