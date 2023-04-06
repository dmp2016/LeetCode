from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        island_num = 1
        not_closed_amount = 0
        for row in range(n):
            for col in range(m):
                if grid[row][col] == 0:
                    is_not_closed = False
                    island_num += 1
                    q = [(row, col)]
                    while q:
                        cur = q.pop()
                        grid[cur[0]][cur[1]] = island_num
                        if cur[0] in (0, n - 1) or cur[1] in (0, m - 1):
                            is_not_closed = True
                        for delta_row, delta_col in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                            if 0 <= cur[0] + delta_row < n and 0 <= cur[1] + delta_col < m and grid[cur[0] + delta_row][cur[1] + delta_col] == 0:
                                q.append((cur[0] + delta_row, cur[1] + delta_col))
                    if is_not_closed:
                        not_closed_amount += 1
        return island_num - 1 - not_closed_amount


t = Solution()
print(t.closedIsland(grid=[[1, 1, 1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 1, 0], [
      1, 0, 1, 0, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 0]]))
print(t.closedIsland(grid=[[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]]))
print(t.closedIsland(grid=[
    [0, 0, 1, 1, 0, 1, 0, 0, 1, 0], 
    [1, 1, 0, 1, 1, 0, 1, 1, 1, 0], 
    [1, 0, 1, 1, 1, 0, 0, 1, 1, 0], 
    [0, 1, 1, 0, 0, 0, 0, 1, 0, 1], 
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 0], 
    [0, 1, 0, 1, 0, 1, 0, 1, 1, 1], 
    [1, 0, 1, 0, 1, 1, 0, 0, 0, 1], 
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 0], 
    [1, 1, 1, 0, 0, 1, 0, 1, 0, 1], 
    [1, 1, 1, 0, 1, 1, 0, 1, 1, 0]]))
