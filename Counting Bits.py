from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]
        k = 1
        while k <= n:
            i = 0
            m = len(res)
            while i < m and k <= n:
                res.append(res[i] + 1)
                k += 1
                i += 1
        return res


test = Solution()
print(test.countBits(50))
