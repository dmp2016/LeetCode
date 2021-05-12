from typing import List
from itertools import accumulate


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = [list(accumulate(matrix[0]))]
        for row in range(1, len(matrix)):
            self.matrix.append(list(accumulate(matrix[row])))
            for col in range(len(matrix[row])):
                self.matrix[-1][col] += self.matrix[row - 1][col]

    def get_sum(self, row: int, col: int) -> int:
        if row < 0 or col < 0:
            return 0
        else:
            return self.matrix[row][col]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return -self.get_sum(row2, col1 - 1) - self.get_sum(row1 - 1, col2) + self.get_sum(row1 - 1, col1 - 1) + self.get_sum(row2, col2)


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
test = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
print(test.sumRegion(2, 1, 4, 3))
print(test.sumRegion(1, 1, 2, 2))
print(test.sumRegion(1, 2, 2, 4))

test = NumMatrix([[-4, -5]])
print(test.sumRegion(0, 0, 0, 0))
print(test.sumRegion(0, 0, 0, 1))
print(test.sumRegion(0, 1, 0, 1))
