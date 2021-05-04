from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:

        def check(A: List[int]) -> bool:
            for ind in range(1, len(A)):
                if A[ind - 1] > A[ind]:
                    return False
            return True

        for ind in range(1, len(nums)):
            if nums[ind - 1] > nums[ind]:
                return check(nums[:ind - 1] + nums[ind:]) or check(nums[:ind] + nums[ind + 1:])
        return True


test = Solution()
print(test.checkPossibility(nums=[4, 2, 3]))
print(test.checkPossibility(nums=[4, 2, 1]))
