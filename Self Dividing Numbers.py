from typing import List


class Solution:
    def check(self, a):
        d = a
        while d > 0:
            r = d % 10
            if r == 0 or a % r != 0:
                return False
            d = d // 10
        return True

    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for i in range(left, right + 1):
            if self.check(i):
                res.append(i)
        return res

    def selfDividingNumbers1(self, left: int, right: int) -> List[int]:
        return [i for i in range(left, right + 1) if self.check(i)]


test = Solution()
print(test.selfDividingNumbers(1, 22))


import datetime as dt

a = dt.datetime.utcnow()
test.selfDividingNumbers(1, 1000000)
print(dt.datetime.utcnow() - a)

a = dt.datetime.utcnow()
test.selfDividingNumbers1(1, 1000000)
print(dt.datetime.utcnow() - a)