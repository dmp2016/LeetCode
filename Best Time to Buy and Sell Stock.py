from concurrent.futures import process
from typing import List
import math


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        res = 0
        for pr in prices[::-1]:
            if res < max_p - pr:
                res = max_p - pr
            if max_p < pr:
                max_p = pr
        return res


test = Solution()
print(test.maxProfit(prices=[7, 1, 5, 3, 6, 4]))
print(test.maxProfit(prices=[7, 6, 4, 3, 1]))
