from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                matrix[row][col] = int(matrix[row][col])


        def check_square(row: int, col: int, n: int) -> bool:
            for cur_row in range(row, row + n):
                if sum(matrix[cur_row][col:col + n]) < n:
                    return False
            return True

        
        cur_n = 1
        left = 0
        right = min(len(matrix), len(matrix[0])) + 1
        # while cur_n < min(len(matrix), len(matrix[0])):
        while left < right - 1:
            cur_n = (left + right) // 2
            check__n = False
            for row in range(len(matrix) - cur_n + 1):
                if not check__n:
                    for col in range(len(matrix[0]) - cur_n + 1):
                        if check_square(row, col, cur_n):
                            check__n = True
                            break
            if check__n:
                left = cur_n
            else:
                right = cur_n
        
        return left ** 2


test = Solution()
print(test.maximalSquare(matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
print(test.maximalSquare(matrix = [["0","1"],["1","0"]]))
print(test.maximalSquare(matrix = [["0"]]))
