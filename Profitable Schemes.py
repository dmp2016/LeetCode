from typing import List
import math
from functools import lru_cache


class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        dyn = [[0] * (minProfit + 1) for _ in range(n + 1)]
        if minProfit == 0:
            dyn[0][0] = 1
        filled = set()
        for i in range(len(group)):
            new_filled = []
            cur_n = group[i]
            cur_profit = profit[i]
            if cur_n <= n:
                if cur_profit <= minProfit:
                    new_filled.append((cur_n, cur_profit, 1))
                else:
                    new_filled.append((cur_n, minProfit, 1))
                for item in filled:
                    next_n = item[0] + cur_n
                    if next_n <= n:
                        if cur_profit + item[1] <= minProfit:
                            new_filled.append((next_n, cur_profit + item[1], dyn[item[0]][item[1]]))
                        else:
                            new_filled.append((next_n, minProfit, dyn[item[0]][item[1]]))
            for item in new_filled:
                filled.add((item[0], item[1]))
                dyn[item[0]][item[1]] = (dyn[item[0]][item[1]] + item[2]) % 1000000007
        return sum(dyn[i][minProfit] for i in range(n + 1)) % 1000000007


t = Solution()
print(t.profitableSchemes(n=5, minProfit=3, group=[2, 2], profit=[2, 3]))
print(t.profitableSchemes(n=10, minProfit=5,
      group=[3, 5, 3, 5], profit=[7, 8, 2, 4]))
print(t.profitableSchemes(n=100, minProfit=10, group=[66, 24, 53, 49, 86, 37, 4, 70, 99, 68, 14, 91, 70, 71, 70, 98, 48, 26, 13, 86, 4, 82, 1, 7, 51, 37, 27, 87, 2, 65, 93, 66, 99, 28, 17, 93, 83, 91, 45, 3, 59, 87, 92, 62, 77, 21, 9, 37, 11, 4, 69, 46, 70, 47, 28, 40, 74, 47, 12, 3, 85, 16, 91, 100, 39, 24, 52, 50, 40, 23, 64, 22, 2, 15, 18, 62, 26, 76, 3, 60, 64, 34, 45, 40, 49,
      11, 5, 8, 40, 71, 12, 60, 3, 51, 31, 5, 42, 52, 15, 36], profit=[8, 4, 8, 8, 9, 3, 1, 6, 7, 10, 1, 10, 4, 9, 7, 11, 5, 1, 7, 4, 11, 1, 5, 9, 9, 5, 1, 10, 0, 10, 4, 1, 1, 1, 6, 9, 3, 6, 2, 5, 4, 7, 8, 5, 2, 3, 0, 6, 4, 5, 9, 9, 10, 7, 1, 8, 9, 6, 0, 2, 9, 2, 2, 8, 6, 10, 3, 4, 6, 1, 10, 7, 5, 4, 8, 1, 8, 5, 5, 4, 1, 1, 10, 0, 8, 0, 1, 11, 5, 4, 7, 9, 1, 11, 1, 0, 1, 6, 8, 3]))
print(t.profitableSchemes(n=100, minProfit=100, group=[24, 23, 7, 4, 26, 3, 7, 11, 1, 7, 1, 3, 5, 26, 26, 1, 13, 12, 2, 1, 7, 4, 1, 27, 13, 16, 26, 18, 6, 1, 1, 7, 16, 1, 6, 2, 5, 9, 19, 28, 1,
      23, 2, 1, 3, 4, 4, 3, 22, 1, 1, 3, 5, 34, 2, 1, 22, 16, 8, 5, 3, 21, 1, 8, 14, 2, 1, 3, 8, 12, 40, 6, 4, 2, 2, 14, 1, 11, 9, 1, 7, 1, 1, 1, 6, 6, 4, 1, 1, 7, 8, 10, 20, 2, 14, 31, 1, 13, 1, 9],
      profit=[5, 2, 38, 25, 4, 17, 5, 1, 4, 0, 0, 8, 13, 0, 20, 0, 28, 1, 22, 7, 10, 32, 6, 37, 0, 11, 6, 11, 23, 20, 13, 13, 6, 2, 36, 1, 0, 9, 4, 5, 6, 14, 20, 1, 13, 6, 33, 0, 22, 1, 17, 12, 10, 1, 19, 13, 8, 1, 0, 17, 20, 9, 8, 6, 2, 2, 1, 4, 22, 11, 3, 2, 6, 0, 40, 0, 0, 7, 1, 0, 25, 5, 12, 7, 19, 4, 12, 7, 4, 4, 1, 15, 33, 14, 2, 1, 1, 61, 4, 5]))
print(t.profitableSchemes(n=64, minProfit=0, group=[80, 40], profit=[88, 88]))
