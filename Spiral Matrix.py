from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        res = []
        for d in range(min((n + 1) // 2, (m + 1) // 2)):
            res += matrix[d][d:m - d]
            res += [item[m - d - 1] for item in matrix[d + 1:(n - d - 1)]]
            if d != n - d - 1:
                res += list(reversed(matrix[n - d - 1][d:m - d]))
            if d != m - d - 1:
                res += [item[d] for item in matrix[n - d - 2:d:-1]]
        return res


test = Solution()
print(test.spiralOrder(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(test.spiralOrder(matrix=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
print(test.spiralOrder(matrix=[[7], [9], [6]]))
