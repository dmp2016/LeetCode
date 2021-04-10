from typing import List
from functools import lru_cache


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        fld = [[-1] * len(matrix[0]) for _ in range(len(matrix))]

        max_size = len(matrix[0]) * len(matrix)
        # @lru_cache(maxsize=max_size)
        def do_rec(row: int, col: int) -> int:
            if fld[row][col] >= 0:
                return fld[row][col]
            cur = matrix[row][col]
            max_path = 0
            if row > 0 and matrix[row - 1][col] > cur:
                max_path = max(max_path, 1 + do_rec(row - 1, col))
            if col > 0 and matrix[row][col - 1] > cur:
                max_path = max(max_path, 1 + do_rec(row, col - 1))
            if col < len(matrix[0]) - 1 and matrix[row][col + 1] > cur:
                max_path = max(max_path, 1 + do_rec(row, col + 1))
            if row < len(matrix) - 1 and matrix[row + 1][col] > cur:
                max_path = max(max_path, 1 + do_rec(row + 1, col))
            fld[row][col] = max_path
            return max_path

        max_path = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                max_path = max(max_path, do_rec(i, j))
                    
        return max_path + 1


test = Solution()
print(test.longestIncreasingPath(matrix=[[9,9,4],[6,6,8],[2,1,1]]))
test = Solution()
print(test.longestIncreasingPath(matrix=[[1]]))
print(test.longestIncreasingPath(matrix=[[1,2]]))
