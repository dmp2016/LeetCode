from typing import List, Tuple


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        step_cnt = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    start = (row, col)
                elif grid[row][col] == 2:
                    end = (row, col)
                elif grid[row][col] == 0:
                    step_cnt += 1

        cur_step = 0
        front = [(start, set())]
        while front:
            new_front = []
            for item in front:
                new_path = item[1].union([item[0]])
                for d_row, d_col in zip((0, 0, -1, 1), (1, -1, 0, 0)):
                    cur = (item[0][0] + d_row, item[0][1] + d_col)
                    if cur not in item[1] and 0 <= cur[0] < len(grid) and 0 <= cur[1] < len(grid[0]) and grid[cur[0]][cur[1]] == 0:
                        if abs(cur[0] - end[0]) + abs(cur[1] - end[1]) <= step_cnt - len(new_path) + 1:
                            new_front.append((cur, new_path))
            if not new_front and front and len(front[0][1]) == step_cnt:
                res = 0
                for item in front:
                    for d_row, d_col in zip((0, 0, -1, 1), (1, -1, 0, 0)):
                        cur = (item[0][0] + d_row, item[0][1] + d_col)
                        if 0 <= cur[0] < len(grid) and 0 <= cur[1] < len(grid[0]) and grid[cur[0]][cur[1]] == 2:
                            res += 1
                return res
            else:
                front = new_front
        return 0


test = Solution()
print(test.uniquePathsIII(grid = [[1,2]]))
print(test.uniquePathsIII(grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]))
print(test.uniquePathsIII(grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]))
print(test.uniquePathsIII(grid=[
    [1,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,2]]))
