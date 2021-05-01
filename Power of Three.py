import math


class Solution:
    def isPowerOfThree1(self, n: int) -> bool:
        if n <= 0:
            return False
        return 3 ** round(math.log(n, 3)) == n

    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        return (3 ** 19) % n == 0


test = Solution()
print(test.isPowerOfThree(27))
print(test.isPowerOfThree(82))
