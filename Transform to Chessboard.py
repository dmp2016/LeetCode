from typing import List


class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        n = len(board)

        rows = [tuple(row) for row in board]
        row_set = set(rows)
        if len(row_set) != 2:
            return -1
        cols = [tuple(board[ind_row][ind_col] for ind_row in range(n)) for ind_col in range(n)]
        col_set = set(cols)
        if len(col_set) != 2:
            return -1

        row1 = row_set.pop()
        row2 = row_set.pop()
        del row_set

        col1 = col_set.pop()
        col2 = col_set.pop()
        del col_set

        r_ones_1 = sum(row1)
        r_ones_2 = sum(row2)

        if not (r_ones_1 + r_ones_2 == n and (r_ones_1 == n // 2 or r_ones_2 == n // 2)):
            return -1

        c_ones_1 = sum(col1)
        c_ones_2 = sum(col2)

        if not (c_ones_1 + c_ones_2 == n and (c_ones_1 == n // 2 or c_ones_2 == n // 2)):
            return -1

        def proc_vec(vec1: List[int], vec2: List[int], vector_list: List[List[int]]) -> int:
            if n & 1:
                vec1_cnt = 0
                for ind in range(n):
                    if vec1 == vector_list[ind]:
                        vec1_cnt += 1

                res = 0
                if vec1_cnt > n - vec1_cnt:
                    row_comp = vec1
                else:
                    row_comp = vec2

                for ind in range(0, n, 2):
                    if row_comp != vector_list[ind]:
                        res += 1
                return res
            else:
                vc1, vc2 = 0, 0
                for ind in range(0, n, 2):
                    if vec1 != vector_list[ind]:
                        vc1 += 1
                    else:
                        vc2 += 1
                return min(vc1, vc2)

        return proc_vec(row1, row2, rows) + proc_vec(col1, col2, cols)


test = Solution()
print(test.movesToChessboard(board=[
    [0, 1, 1, 0], 
    [0, 1, 1, 0], 
    [1, 0, 0, 1], 
    [1, 0, 0, 1]]))
print(test.movesToChessboard(board=[
    [0, 1],
    [1, 0]]))
print(test.movesToChessboard(board=[
    [1, 0],
    [1, 0]]))
print(test.movesToChessboard(board=[
    [1, 0, 0],
    [0, 1, 1],
    [1, 0, 0]]))
print(test.movesToChessboard(board=[
    [1, 0, 0, 1, 1],
    [0, 1, 1, 0, 0],
    [1, 0, 0, 1, 1],
    [0, 1, 1, 0, 0],
    [0, 1, 1, 0, 0]]))
