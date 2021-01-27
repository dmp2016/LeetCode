import math

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        res = 1
        mod = 1000000007
        bt = 2
        btc = 1
        for k in range(2, n + 1):
            if k >= bt:
                bt <<= 1
                btc += 1
            res = ((res << btc) + k)
            if res > mod:
                res %= mod
        return res


test = Solution()
print(test.concatenatedBinary(1))
print(test.concatenatedBinary(3))
print(test.concatenatedBinary(12))
