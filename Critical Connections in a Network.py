from typing import List, Optional
from collections import defaultdict
import sys

sys.setrecursionlimit(2000)


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        v = defaultdict(set)
        for a, b in connections:
            v[a].add(b)
            v[b].add(a)
        cycle_edges = set()
        path = []
        path_ind = dict()
        pd = set()

        def dfs(prev: Optional[int], a: int):
            if a in path_ind:
                cycle_edges.add((path[-1], a))
                cycle_edges.add((a, path[-1]))
                for ind in range(len(path) - 2, path_ind[a] - 1, -1):
                    if (path[ind], path[ind + 1]) not in cycle_edges:
                        cycle_edges.add((path[ind], path[ind + 1]))
                        cycle_edges.add((path[ind + 1], path[ind]))
                    else:
                        break
                for ind in range(path_ind[a], len(path) - 1):
                    if (path[ind], path[ind + 1]) not in cycle_edges:
                        cycle_edges.add((path[ind], path[ind + 1]))
                        cycle_edges.add((path[ind + 1], path[ind]))
                    else:
                        break
            else:
                if a not in pd:
                    path.append(a)
                    path_ind[a] = len(path) - 1
                    for b in v[a]:
                        if b != prev:
                            dfs(a, b)
                    del path_ind[a]
                    path.pop()
                    pd.add(a)

        dfs(None, 0)

        res = []
        for a, b in connections:
            if (a, b) not in cycle_edges:
                res.append([a, b])
        return res


test = Solution()
print(test.criticalConnections1(n=4, connections=[[0, 1], [1, 2], [2, 0], [1, 3]]))
