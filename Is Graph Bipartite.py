from typing import List
from collections import deque


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        vert_cnt = len(graph)
        parts = [-1] * vert_cnt

        not_visited = set(range(0, vert_cnt))
        q = deque()

        while not_visited:
            v0 = not_visited.pop()
            q.append(v0)
            parts[v0] = 0

            while q:
                v = q.popleft()
                cur_part = parts[v]
                for vn in graph[v]:
                    if parts[vn] != cur_part:
                        parts[vn] = 1 - cur_part
                    else:
                        return False
                    if vn in not_visited:
                        not_visited.remove(vn)
                        q.append(vn)
        return True


test = Solution()
print(test.isBipartite([[1,3],[0,2],[1,3],[0,2]]))
print(test.isBipartite([[1,2,3],[0,2],[0,1,3],[0,2]]))
