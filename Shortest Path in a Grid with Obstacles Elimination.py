from typing import List
import math


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        n = len(grid)
        m = len(grid[0])

        used = set()

        cache = dict()
        def do(row: int, col: int, k: int) -> int:
            d = cache.get((row, col, k))
            if d:
                return d
            if row == n or col == m or row == -1 or col == -1 or (row, col) in used or (k == 0 and grid[row][col] == 1):
                cache[(row, col, k)] = math.inf
                return math.inf
            if row == n - 1 and col == m - 1:
                return 0
            new_k = k - grid[row][col]
            used.add((row, col))
            res_cur = min([
                do(row - 1, col, new_k),
                do(row + 1, col, new_k),
                do(row, col - 1, new_k),
                do(row, col + 1, new_k)]) + 1
            used.remove((row, col))
            cache[(row, col, k)] = res_cur
            return res_cur
        
        res = do(0, 0, k)
        return res if res < math.inf else -1            


test = Solution()
print(test.shortestPath(
    grid=[
        [0, 0, 0],
        [1, 1, 0],
        [0, 0, 0],
        [0, 1, 1],
        [0, 0, 0]
        ],
    k=1))

print(test.shortestPath(
    grid=[
        [0,1,1],
        [1,1,1],
        [1,0,0]],
    k = 1))
