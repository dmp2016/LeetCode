from typing import List


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        field = [[0] * 3 for _ in range(3)]
        a = True
        for point in moves:
            field[point[0]][point[1]] = 1 if a else 2
            a = not a
        for i in range(3):
            is_a_win = True
            is_b_win = True
            for j in range(3):
                is_a_win = is_a_win and field[i][j] == 1
                is_b_win = is_b_win and field[i][j] == 2
            if is_a_win:
                return 'A'
            if is_b_win:
                return 'B'

        for i in range(3):
            is_a_win = True
            is_b_win = True
            for j in range(3):
                is_a_win = is_a_win and field[j][i] == 1
                is_b_win = is_b_win and field[j][i] == 2
            if is_a_win:
                return 'A'
            if is_b_win:
                return 'B'

        is_a_win = True
        is_b_win = True
        for i in range(3):
            is_a_win = is_a_win and field[i][i] == 1
            is_b_win = is_b_win and field[i][i] == 2
        if is_a_win:
            return 'A'
        if is_b_win:
            return 'B'

        is_a_win = True
        is_b_win = True
        for i in range(3):
            is_a_win = is_a_win and field[i][2 - i] == 1
            is_b_win = is_b_win and field[i][2 - i] == 2
        if is_a_win:
            return 'A'
        if is_b_win:
            return 'B'

        for i in range(3):
            for j in range(3):
                if field[i][j] == 0:
                    return 'Pending'

        return 'Draw'
