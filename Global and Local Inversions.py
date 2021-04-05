from typing import List


class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        if len(A) <= 2:
            return True
        mc = A[0]
        for ind in range(2, len(A)):
            if mc > A[ind]:
                return False
            mc = max(mc, A[ind - 1])
        return True


test = Solution()
print(test.isIdealPermutation(A=[1, 0, 2]))
print(test.isIdealPermutation(A=[1, 2, 0]))
print(test.isIdealPermutation(A=[2, 0, 1]))
