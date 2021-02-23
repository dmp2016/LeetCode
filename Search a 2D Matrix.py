from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        left, right = 0, n*m - 1
        while left <= right:
            mid = (left + right) // 2
            elem = matrix[mid // m][mid % m]
            if elem == target:
                return True
            elif elem < target:
                left = mid + 1
            else:
                right = mid - 1
        return False


test = Solution()
# print(test.searchMatrix(matrix = [[1,3,5,7]], target = 5))
print(test.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3))
print(test.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13))
