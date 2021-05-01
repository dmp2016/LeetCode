import math


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return math.comb(n + m - 2, m - 1)


test = Solution()
print(test.uniquePaths(m=3, n=7))
print(test.uniquePaths(m=2, n=3))
print(test.uniquePaths(m=3, n=3))
print(test.uniquePaths(m=1, n=1))
