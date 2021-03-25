from typing import List
from collections import deque


class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []
        nrow = len(matrix)
        ncol = len(matrix[0])
        fld = sorted([(matrix[i][j], i, j) for i in range(nrow) for j in range(ncol)])
        tp = [[0] * ncol for i in range(nrow)]
        visited_all = set()
        q = deque()
        for elem in fld:
            row, col = elem[1], elem[2]
            if (row, col) not in visited_all:
                q.append((row, col))
                visited = set()
                stp = 0
                while q:
                    cur = q.popleft()
                    row, col = cur[0], cur[1]
                    if cur not in visited:
                        if cur in visited_all:
                            stp |= tp[row][col]
                        else:
                            h = matrix[row][col]
                            if row == 0 or col == 0:
                                stp |= 1
                            if row == nrow - 1 or col == ncol - 1:
                                stp |= 2
                            if row > 0 and h >= matrix[row - 1][col]:
                                q.append((row - 1, col))
                            if row < nrow - 1 and h >= matrix[row + 1][col]:
                                q.append((row + 1, col))
                            if col > 0 and h >= matrix[row][col - 1]:
                                q.append((row, col - 1))
                            if col < ncol - 1 and h >= matrix[row][col + 1]:
                                q.append((row, col + 1))
                            visited.add(cur)
                for row, col in visited:
                    tp[row][col] = stp
                visited_all.update(visited)
        return [[i, j] for i in range(nrow) for j in range(ncol) if tp[i][j] == 3]


test = Solution()
print(test.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))                    
print(test.pacificAtlantic([[10,10,10],[10,1,10],[10,10,10]]))
