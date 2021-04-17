from typing import List


class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        res = []
        for x, y, r in queries:
            a = 0
            for xi, yi in points:
                if (xi - x) ** 2 + (yi - y) ** 2 <= r ** 2:
                    a += 1
            res.append(a)
        return res


test = Solution()
print(test.countPoints(points=[[1, 3], [3, 3], [5, 3], [2, 2]], queries=[[2, 3, 1], [4, 3, 1], [1, 1, 2]]))
print(test.countPoints(points=[[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]], queries=[[1, 2, 2], [2, 2, 2], [4, 3, 2], [4, 3, 3]]))
