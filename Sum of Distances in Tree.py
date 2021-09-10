from collections import defaultdict
from typing import List, Optional


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = dict()
        for edge in edges:
            graph.setdefault(edge[0], []).append(edge[1])
            graph.setdefault(edge[1], []).append(edge[0])

        path_cnt = dict()
        path_sum = dict()

        def go1(cur_v: int, parent: Optional[int]) -> None:
            neighbors = graph.get(cur_v, [])
            path_cnt[cur_v] = 0
            path_sum[cur_v] = 0
            for cv in neighbors:
                if cv != parent:
                    go1(cv, cur_v)
                    path_cnt[cur_v] += path_cnt[cv] + 1
                    path_sum[cur_v] += path_sum[cv] + path_cnt[cv] + 1

        def go2(cur_v, parent) -> None:
            neighbors = graph.get(cur_v, [])
            for cv in neighbors:
                if cv != parent:
                    path_sum[cv] = path_sum[cur_v] - 1 - 2 * path_cnt[cv] + path_cnt[cur_v]
                    path_cnt[cv] = n - 1
                    # path_sum[cv] = path_sum[cv] + 1 + (path_sum[cur_v] - 1 - path_cnt[cv] - path_sum[cv]) + (path_cnt[cur_v] - 1 - path_cnt[cv])
                    # path_cnt[cv] = path_cnt[cv] + 1 + (path_cnt[cur_v] - 1 - path_cnt[cv])

            for cv in neighbors:
                if cv != parent:
                    go2(cv, cur_v)

        go1(0, None)
        go2(0, None)

        return [path_sum[i] for i in range(n)]


test = Solution()
print(test.sumOfDistancesInTree(n=6, edges=[[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]))
print(test.sumOfDistancesInTree(n=1, edges=[]))
print(test.sumOfDistancesInTree(n=2, edges=[[1, 0]]))
