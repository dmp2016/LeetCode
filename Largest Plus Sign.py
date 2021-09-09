from typing import List


class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        field = []
        for _ in range(n):
            field.append([1] * n)
        for mine in mines:
            field[mine[0]][mine[1]] = 0

        pf = []
        for _ in range(n):
            pf.append([10000] * n)

        for x in range(n):
            r = 0
            for y in range(n):
                if field[x][y] == 0:
                    r = 0
                else:
                    r += 1
                pf[x][y] = min(pf[x][y], r)
            r = 0
            for y in range(n - 1, -1, -1):
                if field[x][y] == 0:
                    r = 0
                else:
                    r += 1
                pf[x][y] = min(pf[x][y], r)

        for y in range(n):
            r = 0
            for x in range(n):
                if field[x][y] == 0:
                    r = 0
                else:
                    r += 1
                pf[x][y] = min(pf[x][y], r)
            r = 0
            for x in range(n - 1, -1, -1):
                if field[x][y] == 0:
                    r = 0
                else:
                    r += 1
                pf[x][y] = min(pf[x][y], r)

        res = 0
        for x in range(n):
            res = max(res, max(pf[x]))

        return res


test = Solution()
print(test.orderOfLargestPlusSign(n=5, mines=[[4, 2]]))
print(test.orderOfLargestPlusSign(n=1, mines=[[0, 0]]))
