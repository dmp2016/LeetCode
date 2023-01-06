from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        res = 0
        for a in sorted(costs):
            if a <= coins:
                coins -= a
                res += 1
        return res


test = Solution()
print(test.maxIceCream(costs=[1, 3, 2, 4, 1], coins=7))
print(test.maxIceCream(costs=[10, 6, 8, 7, 7, 8], coins=5))
print(test.maxIceCream(costs=[1, 6, 3, 1, 2, 5], coins=20))
