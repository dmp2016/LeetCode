from typing import List


class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        difs = [A[ind + 1] - A[ind] for ind in range(len(A) - 1)]
        res = 0
        cur = difs[0]
        n = 1
        for elem in difs[1:]:
            if elem == cur:
                n += 1
            else:
                if n > 1:
                    res += (n - 1) * n // 2
                n = 1
                cur = elem
        if n > 1:
            res += (n - 1) * n // 2
        return res


test = Solution()
print(test.numberOfArithmeticSlices(A=[1, 2, 3, 4]))
