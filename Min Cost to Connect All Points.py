from typing import List, FrozenSet
from functools import lru_cache
import math

# TLE

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        v_all = frozenset([(point[0], point[1]) for point in points])

        @lru_cache
        def do_rec(v_set: FrozenSet) -> int:
            if not v_set:
                return 0

            res = math.inf
            v_set_comp = v_all.difference(v_set)
            for v1 in v_set:
                v_set_new = frozenset(v_set.difference([v1]))
                for v2 in v_set_comp:
                    a = abs(v1[0] - v2[0]) + abs(v1[1] - v2[1])
                    res_new = a + do_rec(v_set_new)
                    if res > res_new:
                        res = res_new
            return res
        
        return do_rec(v_all.difference([(points[0][0], points[0][1])]))


test = Solution()
print(test.minCostConnectPoints(points=[[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]))
print(test.minCostConnectPoints(points=[[3, 12], [-2, 5], [-4, 1]]))
