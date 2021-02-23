from typing import List
from bisect import bisect_right


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def do_search(row1: int, col1: int, row2: int, col2: int) -> bool:
            if row2 > len(matrix) - 1 or col2 > len(matrix[0]) - 1:
                return False
            if row1 == row2:
                ind = bisect_right(matrix[row1][col1:col2 + 1], target)
                return ind > 0 and matrix[row1][col1 + ind - 1] == target
            if col1 == col2:
                ind = bisect_right([matrix[row][col1] for row in range(row1, row2 + 1)], target)
                return ind > 0 and matrix[row1 + ind - 1][col1] == target
            left, right = 0, min(row2 - row1, col2 - col1)
            if matrix[row1 + left][col1 + left] == target:
                return True
            if matrix[row1 + left][col1 + left] > target:
                return False
            if target < matrix[row1 + right][col1 + right]:
                while left < right - 1:
                    mid = (left + right) // 2
                    if matrix[row1 + mid][col1 + mid] < target:
                        left = mid
                    else:
                        right = mid
            return do_search(row1 + right, col1 + right, row2, col2) or \
                do_search(row1 + right, col1, row2, col1 + right - 1) or \
                do_search(row1, col1 + right, row1 + right - 1, col2)
        
        return do_search(0, 0, len(matrix) - 1, len(matrix[0]) - 1)


test = Solution()
# print(test.searchMatrix(matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5))
# print(test.searchMatrix(matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20))
# print(test.searchMatrix(matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 25))
# print(test.searchMatrix(matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 30))
print(test.searchMatrix(matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]], target = 15))
# print(test.searchMatrix(matrix = [[1,4,7,11,15]], target = 15))