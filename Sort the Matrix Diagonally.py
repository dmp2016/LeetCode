from typing import List


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        for i in range(0, n):
            temp = sorted([mat[i + j][j] for j in range(0, min(m, n - i))])
            for j in range(0, min(m, n - i)):
                mat[i + j][j] = temp[j]
        for i in range(1, m):
            temp = sorted([mat[j][i + j] for j in range(0, min(n, m - i))])
            for j in range(0, min(n, m - i)):
                mat[j][i + j] = temp[j]
        return mat


test = Solution()
print(test.diagonalSort(mat=[[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]]))
