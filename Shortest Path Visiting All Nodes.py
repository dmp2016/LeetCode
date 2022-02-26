from typing import List, Tuple
from math import inf
from collections import Counter


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:        
        if len(graph) in (0, 1):
            return 0
        
        def bfs(v: int):
            step = 0
            front = {(v, frozenset([v]))}
            used = {(v, frozenset([v]))}
            while True:
                new_front = set()
                step += 1
                for elem in front:
                    r = list(elem[1])
                    for v in graph[elem[0]]:
                        r.append(v)
                        fz = frozenset(r)
                        if len(fz) == len(graph):
                            return step
                        if not (v, fz) in used:
                            used.add((v, fz))
                            new_front.add((v, fz))
                        r.pop()
                front = new_front

        res = inf
        for ind in range(len(graph)):
            res = min(res, bfs(ind))
        return res

test = Solution()
# print(test.shortestPathLength(graph=[[1, 2, 3], [0], [0], [0]]))
# print(test.shortestPathLength(graph=[[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]]))
# print(test.shortestPathLength(graph=[[7],[3],[3,9],[1,2,4,5,7,11],[3],[3],[9],[3,10,8,0],[7],[11,6,2],[7],[3,9]]))
print(test.shortestPathLength(graph=[[1,2,3,4,5,6,7,8,9],[0,2,3,4,5,6,7,8,9],[0,1,3,4,5,6,7,8,9],[0,1,2,4,5,6,7,8,9],[0,1,2,3,5,6,7,8,9],[0,1,2,3,4,6,7,8,9],[0,1,2,3,4,5,7,8,9],[0,1,2,3,4,5,6,8,9],[0,1,2,3,4,5,6,7,9,10],[0,1,2,3,4,5,6,7,8,11],[8],[9]]))
