class Solution:
    def totalNQueens(self, n: int) -> int:
        bcols = set()
        bdiags1 = set()
        bdiags2 = set()
        self.res = 0
        qcols = [0] * n


        def check_row(row: int) -> None:
            if row == n:
                self.res += 1
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
        return self.res


test = Solution()
print(test.totalNQueens(2))
print(test.totalNQueens(3))
print(test.totalNQueens(4))
print(test.totalNQueens(5))
print(test.totalNQueens(9))
