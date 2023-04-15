from typing import List
from functools import lru_cache


class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        for i in range(len(piles)):
            piles[i] = piles[i][:k]

        @lru_cache(None)
        def do_rec(cur_ind: int, k_local: int) -> int:
            if cur_ind >= len(piles) or k_local <= 0:
                return 0
            cur_sum = 0
            res = do_rec(cur_ind + 1, k_local)
            for i in range(len(piles[cur_ind])):
                k_local -= 1
                if k_local >= 0:
                    cur_sum += piles[cur_ind][i]
                    res = max(res, cur_sum + do_rec(cur_ind + 1, k_local))
            return res

        return do_rec(0, k)


t = Solution()
print(t.maxValueOfCoins(piles=[[1, 100, 3], [7, 8, 9]], k=2))
print(t.maxValueOfCoins(piles=[[100], [100], [100], [
      100], [100], [100], [1, 1, 1, 1, 1, 1, 700]], k=7))
print(t.maxValueOfCoins(
    piles=[[37, 88], [51, 64, 65, 20, 95, 30, 26], [9, 62, 20], [44]], k=9))
