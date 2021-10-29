from collections import defaultdict
from typing import DefaultDict, List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        graph = defaultdict(set)

        for i in range(len(grid)):
            row = grid[i]
            for j in range(len(row)):
                item = row[j]
                if item in (1, 2):
                    if j < len(row) - 1 and grid[i][j + 1] in (1, 2):
                        graph[(i, j)].add((i, j + 1))
                        graph[(i, j + 1)].add((i, j))
                    if i < len(grid) - 1 and grid[i + 1][j] in (1, 2):
                        graph[(i, j)].add((i + 1, j))
                        graph[(i + 1, j)].add((i, j))

        rotten_cnt = 0
        fresh_cnt = 0
        front = set()
        for i in range(len(grid)):
            row = grid[i]
            for j in range(len(row)):
                item = grid[i][j]
                if item == 1:
                    fresh_cnt += 1
                elif item == 2:
                    rotten_cnt += 1
                    front.add((i, j))
        step_cnt = 0
        rotten_set = front.copy()
        while fresh_cnt > 0:
            step_cnt += 1
            new_front = set()
            old_fresh_cnt = fresh_cnt
            for v in front:
                for vn in graph[v]:
                    if vn not in rotten_set:
                        fresh_cnt -= 1
                        rotten_set.add(vn)
                        new_front.add(vn)
            if old_fresh_cnt == fresh_cnt:
                return -1
            front = new_front
        return step_cnt


test = Solution()
print(test.orangesRotting(grid=[[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
print(test.orangesRotting(grid=[[2, 1, 1], [0, 1, 1], [1, 0, 1]]))
print(test.orangesRotting(grid=[[0, 2]]))
print(test.orangesRotting(grid=[[1], [2]]))
