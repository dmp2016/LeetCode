from typing import List
import math
import functools


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        if len(points) <= 2:
            return len(points)

        @functools.lru_cache(maxsize=None)
        def get_c(ind1: int, ind2: int):
            d1 = points[ind1][0] - points[ind2][0]
            d2 = points[ind1][1] - points[ind2][1]
            c0 = math.gcd(d1, d2)
            d1 //= c0
            d2 //= c0
            if d1 < 0:
                d1, d2 = -d1, -d2
            return (d1, d2)

        res = 2
        for ind1 in range(len(points) - 2):
            for ind2 in range(ind1 + 1, len(points) - 1):
                p1 = get_c(ind1, ind2)
                t = 2
                for ind3 in range(ind2 + 1, len(points)):
                    p2 = get_c(ind2, ind3)
                    if p1 == p2 or p1[0] == p2[0] == 0 or p1[1] == p2[1] == 0:
                        t += 1
                res = max(res, t)
        return res


test = Solution()
# print(test.maxPoints(points=[[1, 1], [2, 2], [3, 3]]))
# print(test.maxPoints(points=[[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]))
print(test.maxPoints(points=[[4, 5], [4, -1], [4, 0]]))
