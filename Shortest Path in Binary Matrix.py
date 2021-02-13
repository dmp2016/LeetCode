from typing import Iterator, List, Tuple
from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]:
            return -1

        rows = len(grid)
        cols = len(grid[0])
        def get_neighbour(row: int, col: int) -> Iterator[Tuple[int, int]]:
            for dr, dc in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < rows and 0 <= new_col < cols and not grid[new_row][new_col]:
                    yield (new_row, new_col)

        visited = set([(0, 0)])
        distances = {(0, 0) : 1}
        q = deque()
        q.append((0, 0))
        while q:
            v = q.popleft()
            for vn in get_neighbour(v[0], v[1]):
                if vn not in visited:
                    visited.add(vn)
                    distances[vn] = distances[v] + 1
                    q.append(vn)
        return distances.get((rows - 1, cols - 1), -1)


test = Solution()
print(test.shortestPathBinaryMatrix([[0,1],[1,0]]))
print(test.shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]]))
print(test.shortestPathBinaryMatrix([[1,0,0],[1,1,0],[1,1,0]]))
