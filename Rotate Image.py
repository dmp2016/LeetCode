from typing import List


class Solution:
    def rotate1(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n // 2):
            for j in range(n - 2 * i - 1):
                matrix[i][i + j], matrix[i + j][n - 1 - i], matrix[n - 1 - i][(n - 1 - i) - j], matrix[(n - 1 - i) - j][i] = \
                    matrix[(n - 1 - i) - j][i], matrix[i][i + j], matrix[i + j][n - 1 - i], matrix[n - 1 - i][(n - 1 - i) - j]

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Transpose
        n = len(matrix)
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix[i])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Reverse each row
        for i in range(len(matrix)):
            for j in range(len(matrix[i]) // 2):
                matrix[i][j], matrix[i][n - 1 - j] = matrix[i][n - 1 - j], matrix[i][j]


test = Solution()
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(test.rotate(matrix))
print(matrix)
matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
print(test.rotate(matrix))
print(matrix)
matrix = [[1]]
print(test.rotate(matrix))
print(matrix)
matrix = [[1, 2], [3, 4]]
print(test.rotate(matrix))
print(matrix)
