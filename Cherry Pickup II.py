from typing import List
from functools import cache


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        row_max = len(grid)
        col_max = len(grid[0])

        @cache
        def run(row: int, col1: int, col2: int) -> int:
            if not (0 <= row < row_max) or not (0 <= col1 < col_max) or not (0 <= col2 < col_max):
                return 0
            cur = grid[row][col1] + grid[row][col2] if col1 != col2 else grid[row][col1]
            return cur + max([run(row + 1, col1 + delta1, col2 + delta2) for delta1 in (-1, 0, 1) for delta2 in (-1, 0, 1)])

        return run(0, 0, col_max - 1)


test = Solution()
print(test.cherryPickup([[3,1,1],[2,5,1],[1,5,5],[2,1,1]]))
print(test.cherryPickup([[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]))
