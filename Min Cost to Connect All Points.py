from typing import List, FrozenSet
import math


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        v_all = [(point[0], point[1]) for point in points]

        self.res = math.inf

        def do_rec(v_set: FrozenSet) -> int:
            if not v_set:
                return 0

test = Solution()
print(test.minCostConnectPoints(points=[[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]))
print(test.minCostConnectPoints(points=[[3, 12], [-2, 5], [-4, 1]]))
