from typing import List


class Solution:
    def numPoints(self, points: List[List[int]], r: int) -> int:
        cnt = 0
        for x, y in points:
            cnt += 1 if x*x + y*y <= r*r else 0
        return cnt


test = Solution()
print(test.numPoints(points=[[1,2],[3,5],[1,-1],[2,3],[4,1],[1,3]], r=2))
