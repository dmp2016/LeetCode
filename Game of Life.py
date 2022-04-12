from typing import List
from itertools import product


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        for x in range(n):
            for y in range(m):
                sm = 0
                for dx, dy in product((-1, 0, 1), (-1, 0, 1)):
                    if (dx != 0 or dy != 0) and 0 <= x + dx < n and 0 <= y + dy < m:
                        sm += board[x + dx][y + dy] & 1
                if sm < 2:
                    pass
                elif sm == 2:
                    board[x][y] |= (board[x][y] & 1) << 1
                elif sm == 3:
                    board[x][y] |= 2
                else:
                    pass
        for x in range(n):
            for y in range(m):
                board[x][y] = board[x][y] >> 1


test = Solution()
board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
test.gameOfLife(board)
print(board)
        
board = board = [[1, 1], [1, 0]]
test.gameOfLife(board)
print(board)
