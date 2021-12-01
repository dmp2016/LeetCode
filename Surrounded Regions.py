from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def do_cell_o(row_num: int, col_num: int) -> None:
            q = [(row_num, col_num)]
            while q:
                cur = q.pop()
                board[cur[0]][cur[1]] = 'P'
                for d_row, d_col in zip((0, 0, -1, 1), (1, -1, 0, 0)):
                    new_row = cur[0] + d_row
                    new_col = cur[1] + d_col
                    if 0 <= new_row < len(board) and 0 <= new_col < len(board[0]) and board[new_row][new_col] == 'O':
                        q.append((new_row, new_col))

        for row_num in (0, len(board) - 1):
            for col_num in range(len(board[0])):
                if board[row_num][col_num] == "O":
                    do_cell_o(row_num, col_num)

        for row_num in range(len(board)):
            for col_num in (0, len(board[0]) - 1):
                if board[row_num][col_num] == "O":
                    do_cell_o(row_num, col_num)

        for row_num in range(len(board)):
            for col_num in range(len(board[0])):
                if board[row_num][col_num] == 'O':
                    board[row_num][col_num] = 'X'
                elif board[row_num][col_num] == 'P':
                    board[row_num][col_num] = 'O'



test = Solution()
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
test.solve(board)
print(board)
