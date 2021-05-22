from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        bcols = set()
        bdiags1 = set()
        bdiags2 = set()
        res = []
        qcols = [0] * n

        def get_res() -> List[str]:
            return [''.join(['Q' if col == qcols[row] else '.' 
                for col in range(n)]) for row in range(n)]

        def check_row(row: int) -> None:
            if row == n:
                res.append(get_res())
                return
            col = 0
            while True:
                while col < n and (col in bcols or (row - col) in bdiags1 or (col + row) in bdiags2):
                    col += 1
                if col < n:
                    bcols.add(col)
                    bdiags1.add(row - col)
                    bdiags2.add(col + row)
                    qcols[row] = col
                    check_row(row + 1)
                    bcols.remove(col)
                    bdiags1.remove(row - col)
                    bdiags2.remove(col + row)
                    col += 1
                else:
                    break
        check_row(0)
        return res


test = Solution()
print(test.solveNQueens(2))
print(test.solveNQueens(3))
print(test.solveNQueens(4))
print(test.solveNQueens(5))
print(test.solveNQueens(9))
