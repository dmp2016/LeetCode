from typing import List


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        my_edges = dict()
        for edge in edges:
            my_edges.setdefault(edge[0], []).append(edge[1])
            my_edges.setdefault(edge[1], []).append(edge[0])
        v_set = set(range(n))
        visited = set()
        sum_con = 0
        sum_sq = 0
        while v_set:
            q = [v_set.pop()]
            v_cnt = 0
            while q:
                v = q.pop()
                if v not in visited:
                    v_cnt += 1
                    visited.add(v)
                    for v_next in my_edges.get(v, []):
                        if v_next not in visited:
                            q.append(v_next)
            sum_con += v_cnt
            sum_sq += v_cnt ** 2

        return (sum_con ** 2 - sum_sq) // 2

test = Solution()
print(test.countPairs(n=3, edges=[[0, 1], [0, 2], [1, 2]]))
print(test.countPairs(n=7, edges=[[0, 2], [0, 5], [2, 4], [1, 6], [5, 4]]))
