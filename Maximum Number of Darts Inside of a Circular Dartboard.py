from typing import List
import math


class Solution:
    def numPoints(self, points: List[List[int]], r: int) -> int:
        points = [complex(x, y) for x, y in points]

        def get_cnt(c: complex) -> int:
            return sum([1 for x in points if abs(x - c) <= r + 0.0000001])

        cnt = 0
        for ind1 in range(len(points)):
            for ind2 in range(ind1 + 1, len(points)):
                x1 = points[ind1]
                x2 = points[ind2]
                if abs(x1 - x2) <= 2 * r:
                    d = (x2 - x1) / 2
                    v = complex(d.imag, -d.real)
                    vr2 = math.sqrt((r * r - math.pow(abs(d), 2)))
                    v = vr2 * v / abs(v)
                    cnt = max([cnt, get_cnt(x1 + d + v), get_cnt(x1 + d - v)])
        return cnt if cnt > 0 else 1


test = Solution()
print(test.numPoints(points=[[1,2],[3,5],[1,-1],[2,3],[4,1],[1,3]], r=2))
print(test.numPoints(points = [[-3,0],[3,0],[2,6],[5,4],[0,9],[7,8]], r = 5))
print(test.numPoints(points = [[-2,0],[2,0],[0,2],[0,-2]], r = 1))
print(test.numPoints(points = [[1,2],[3,5],[1,-1],[2,3],[4,1],[1,3]], r = 2))
