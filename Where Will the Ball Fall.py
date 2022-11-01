from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        res = []
        cur = True
        n_row = len(grid)
        n_col = len(grid[0])
        for start_col in range(n_col):
            is_top = True
            row, col = 0, start_col
            while True:
                if is_top:
                    if grid[row][col] == 1:
                        new_col = col + 1
                    else:
                        new_col = col - 1
                    if new_col in (-1, n_col) or grid[row][new_col] == -grid[row][col]:
                        res.append(-1)
                        break
                    else:
                        col = new_col
                        is_top = False
                else:
                    row += 1
                    is_top = True
                if row == n_row:
                    res.append(col)
                    break
        
        return res

test = Solution()
print(test.findBall(grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]))
print(test.findBall(grid = [[-1]]))
print(test.findBall(grid = [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]))
