from typing import List
import math


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dist = [[math.inf] * i for i in range(1, len(triangle) + 1)]
        dist[0][0] = triangle[0][0]
        for lev in range(len(triangle) - 1):
            for i in range(lev + 1):
                dist[lev + 1][i] = min(dist[lev + 1][i], dist[lev][i] + triangle[lev + 1][i])
                dist[lev + 1][i + 1] = min(dist[lev + 1][i + 1], dist[lev][i] + triangle[lev + 1][i + 1])
        return min(dist[-1])


test = Solution()
print(test.minimumTotal(triangle=[[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
print(test.minimumTotal(triangle=[[-10]]))
