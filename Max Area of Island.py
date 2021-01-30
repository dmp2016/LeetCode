from collections import defaultdict
from typing import List


class Solution1:
    # ВFS
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        cnt = 2
        sq = defaultdict(int)

        def do_prop(i: int, j: int):
            if i >= 0 and j >= 0 and i < len(grid) and j < len(grid[i]):
                if grid[i][j] == 1:
                    grid[i][j] = cnt
                    sq[cnt] += 1
                    do_prop(i - 1, j)
                    do_prop(i, j - 1)
                    do_prop(i + 1, j)
                    do_prop(i, j + 1)


        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    do_prop(i, j)
                    cnt += 1
        return max(sq.values(), default=0)


class Solution:
    # Use parts graph and BFS. Faster.
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        cnt = 1
        sq = defaultdict(int)
        edges = defaultdict(list)

        def get_cell(i, j):
            return -1 if i < 0 or j < 0 else grid[i][j]
            
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    if get_cell(i, j - 1) > 1:
                        grid[i][j] = get_cell(i, j - 1)
                    elif get_cell(i - 1, j) > 1:
                        grid[i][j] = get_cell(i - 1, j)
                    else:
                        cnt += 1
                        grid[i][j] = cnt
                    sq[grid[i][j]] += 1
                if grid[i][j] > 1:
                    if get_cell(i, j - 1) > 1:
                        edges[grid[i][j]].append(get_cell(i, j - 1))
                        edges[get_cell(i, j - 1)].append(grid[i][j])
                    if get_cell(i - 1, j) > 1:
                        edges[grid[i][j]].append(get_cell(i - 1, j))
                        edges[get_cell(i - 1, j)].append(grid[i][j])


        area_sq = []
        vertex = set(range(2, cnt + 1))
        visited = set()
        while len(vertex) > 0:
            s = 0
            queue = []            
            queue.append(vertex.pop())
            while queue:
                v1 = queue.pop()
                if v1 not in visited:
                    vertex.discard(v1)
                    visited.add(v1)
                    s += sq[v1]
                    queue.extend(edges[v1])
            area_sq.append(s)

        return max(area_sq) if sq else 0



test = Solution()

print(test.maxAreaOfIsland([
 [0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]))

print(test.maxAreaOfIsland([
 [0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,1,1,1,1,1,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]))

print(test.maxAreaOfIsland([[0,0,0,0,0,0,0,0]]))

print(test.maxAreaOfIsland([
    [0,0,0,0,1,0,1,1,0,0,1,0,1,1,0,1,1,1,0,1,1,1,0,1,0,0,0,0,0,0,0,0,0,1,0,0,1,1,0,0,0,1,1,1,1,1,1,0,1,1],
    [0,1,0,0,0,0,1,1,1,0,1,1,0,0,0,1,0,1,1,1,0,0,1,0,1,0,0,1,0,0,0,1,1,1,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1],
    [1,0,0,0,0,0,0,1,1,1,1,0,1,1,0,0,0,0,1,0,0,1,0,0,1,1,1,0,0,0,0,0,1,1,1,0,0,1,1,1,0,1,1,0,1,0,1,1,1,1],
    [0,0,0,0,1,1,1,0,1,1,0,1,0,0,0,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0,1,1,0,0,1,1,1,0,1,1,1,1,0,1,1,0,0,0,1,1],
    [0,0,0,0,1,1,1,1,0,1,1,0,0,1,1,1,0,1,1,1,0,1,1,0,0,0,1,0,1,1,1,1,1,0,1,1,0,1,1,0,1,0,0,0,0,0,1,0,0,1],
    [0,0,1,1,1,0,1,0,0,0,1,0,0,0,0,0,1,0,1,0,0,1,0,1,0,0,1,1,1,0,1,1,1,1,1,0,1,0,1,1,1,1,0,0,0,0,0,1,0,1],
    [0,1,0,1,0,0,1,0,0,0,0,1,1,1,1,1,0,1,1,1,1,1,0,0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,1,0,0,0,0,1,1,0,1,1,0],
    [0,1,0,0,1,1,1,1,0,1,1,0,1,0,1,0,0,0,1,0,0,0,0,0,1,0,1,1,0,1,0,0,1,0,1,1,1,0,1,0,0,1,1,1,0,0,1,0,1,0],
    [0,1,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,1,0,1,0,0,0,1,0,0,0,1,0,1,0,0,1,0,0,0,0,0,0,1,1,0,1,0,0,1,0,0]]))
