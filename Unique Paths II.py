from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[-1] * m for _ in range(n)]

        if obstacleGrid[-1][-1] == 1 or obstacleGrid[0][0] == 1:
            return 0

        dp[-1][-1] = 1

        def get(row: int, col: int) -> int:
            if row >= n or col >= m or obstacleGrid[row][col] == 1:
                return 0
            elif dp[row][col] >= 0:
                return dp[row][col]
            else:
                dp[row][col] = get(row + 1, col) + get(row, col + 1)
                return dp[row][col]

        return get(0, 0)


test = Solution()
print(test.uniquePathsWithObstacles(obstacleGrid=[[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
print(test.uniquePathsWithObstacles(obstacleGrid=[[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
print(test.uniquePathsWithObstacles(obstacleGrid=[[0, 1], [0, 0]]))
