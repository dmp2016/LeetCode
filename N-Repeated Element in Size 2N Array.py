from typing import List


class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        A.sort()
        x = A[0]
        for i in range(1, len(A)):
            if x == A[i]:
                return x
            x = A[i]


test = Solution()
print(test.repeatedNTimes([1, 2, 3, 3]))
print(test.repeatedNTimes([5,1,5,2,5,3,5,4]))
