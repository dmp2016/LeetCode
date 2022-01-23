from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ms = '123456789'
        ums = []
        for k in range(len(str(low)), len(str(high)) + 1):
            for i in range(0, 9 - k + 1):
                ums.append(int(ms[i:i + k]))
        ums = list(map(int, ums))
        ums.sort()
        res = []
        for a in ums:
            if a > high:
                break
            if a >= low:
                res.append(a)
        return res


test = Solution()
print(test.sequentialDigits(low=100, high=300))
print(test.sequentialDigits(low=1000, high=13000))
