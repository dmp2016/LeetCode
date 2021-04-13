from typing import List


class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        res = list(range(1, n - k + 1))
        a, b, = n, n - k + 1
        for i in range(k):
            if i & 1:
                res.append(b)
                b += 1
            else:
                res.append(a)
                a -= 1
        return res


test = Solution()
# print(test.constructArray(n = 3, k = 1))
print(test.constructArray(n = 3, k = 2))
print(test.constructArray(n = 5, k = 4))
