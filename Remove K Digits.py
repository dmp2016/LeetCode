from itertools import combinations
from math import inf


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        if k == n:
            return '0'
        res = ''
        st = 0
        while k > 0 and st < n:
            md = num[st]
            mdi = st
            if st + 1 < n:
                for i in range(st + 1, min(st + k + 1, n)):
                    if md > num[i]:
                        md = num[i]
                        mdi = i
                res += md
                k -= mdi - st
                st = mdi + 1
            else:
                break
        res += num[st:]
        if k > 0:
            res = res[:-k]
        return str(int(res))


test = Solution()
print(test.removeKdigits(num="1432219", k=3))
print(test.removeKdigits(num="10200", k=1))
print(test.removeKdigits(num="20", k=2))
print(test.removeKdigits(num="1111", k=2))
print(test.removeKdigits(num="1173", k=2))
