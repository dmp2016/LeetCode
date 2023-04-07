from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        cells = 0
        for row in range(n):
            for col in range(m):
                if grid[row][col] == 1:
                    is_closed = True
                    cur_cells = 0
                    q = [(row, col)]
                    grid[row][col] = 2
                    while q:
                        cur = q.pop()
                        cur_cells += 1
                        if cur[0] in (0, n - 1) or cur[1] in (0, m - 1):
                            is_closed = False
                        for delta_row, delta_col in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                            if 0 <= cur[0] + delta_row < n and 0 <= cur[1] + delta_col < m and grid[cur[0] + delta_row][cur[1] + delta_col] == 1:
                                grid[cur[0] + delta_row][cur[1] + delta_col] = 2
                                q.append(
                                    (cur[0] + delta_row, cur[1] + delta_col))
                    if is_closed:
                        cells += cur_cells
        return cells


t = Solution()
print(t.numEnclaves(
    grid=[[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]))
print(t.numEnclaves(
    grid=[[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]))
print(t.numEnclaves(
    grid=[
        [0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0], 
        [1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1], 
        [1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1], 
        [1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0], 
        [1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1], 
        [1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0], 
        [0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0], 
        [0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0], 
        [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1], 
        [1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0]]))
