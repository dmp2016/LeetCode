from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        nrow = len(grid)
        ncol = len(grid[0])
        sz = nrow * ncol

        def get(ind: int) -> int:
            return grid[ind // ncol][ind % ncol]

        def set(ind: int, val: int) -> int:
            grid[ind // ncol][ind % ncol] = val

        k %= sz
        if not k:
            return grid
        for _ in range(k):
            p = sz - 2
            while p >= 0:
                tmp1 = get(p + 1)
                tmp2 = get(p)
                set(p + 1, tmp2)
                set(p, tmp1)
                p -= 1
        return grid


test = Solution()
print(test.shiftGrid(grid=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], k=1))
print(test.shiftGrid(grid=[[3, 8, 1, 9], [19, 7, 2,5 ], [4, 6, 11, 10], [12, 0, 21, 13]], k=4))
print(test.shiftGrid(grid=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], k=2))
print(test.shiftGrid(grid=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], k=3))
print(test.shiftGrid([[1],[2],[3],[4],[7],[6],[5]], 23))
