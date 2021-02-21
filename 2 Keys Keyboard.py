import math

class Solution:
    def minSteps(self, n: int) -> int:
        cnt = 0
        dv = 2
        while n > 1:
            while n % dv == 0:
                cnt += dv
                n //= dv
            dv += 1
        return cnt


test = Solution()
print(test.minSteps(3))
