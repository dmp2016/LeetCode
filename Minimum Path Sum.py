from typing import List
from functools import lru_cache
import math


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:        
        n, m = len(grid), len(grid[0])

        @lru_cache
        def do_rec(row, col):
            if row == n - 1 and col == m - 1:
                return grid[row][col]
            res = math.inf
            if row < n - 1:
                res = min(res, do_rec(row + 1, col))
            if col < m - 1:
                res = min(res, do_rec(row, col + 1))
            return res + grid[row][col]
        
        return do_rec(0, 0)



test = Solution()
print(test.minPathSum(grid=[[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
print(test.minPathSum(grid=[[1, 2, 3], [4, 5, 6]]))
